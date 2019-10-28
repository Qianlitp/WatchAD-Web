#!/usr/bin/python3
# coding: utf-8


import re
from database.MongoHelper import MongoHelper
from config.database_config import MongoConfig
from application.common.common import datetime_to_utc, utc_to_datetime
from bson.objectid import ObjectId
from application.modules.Alert import Alert
from application.modules.Graph import graph_map


class Activity(object):
    def __init__(self):
        self.activity_mongo = MongoHelper(MongoConfig.activities_collection)
        self.alert = Alert()

    def list(self, data: dict) -> list:
        """
            返回威胁活动列表
        """
        page = data["page"]
        del data["page"]
        query = self.get_filter_data(data)
        search = self.activity_mongo.find_all(query)
        start = (page - 1) * 10
        fetcher = search.sort("end_time", -1).skip(start).limit(10)

        result = []
        for each in fetcher:
            each["start_time"] = datetime_to_utc(each["start_time"])
            each["end_time"] = datetime_to_utc(each["end_time"])
            each["desc_data"] = self._get_desc_data(each["_id"], each["description"])
            result.append(each)
        return result

    def list_naive(self, invasion_id: ObjectId) -> list:
        query = {
            "invasion_id": invasion_id
        }
        search = self.activity_mongo.find_all(query)
        fetcher = search.sort("end_time", -1)
        result = []
        for each in fetcher:
            each["start_time"] = datetime_to_utc(each["start_time"])
            each["end_time"] = datetime_to_utc(each["end_time"])
            each["desc_data"] = self._get_desc_data(each["_id"], each["description"])
            result.append(each)
        return result

    def related_count(self, entry_type: str, domain: str, name: str) -> int:
        """
            查询实体相关威胁活动记录数量
        """
        if entry_type == "user":
            alert_query = {
                "domain": domain,
                "$or": [
                    {
                        "form_data.source_user_name": name
                    },
                    {
                        "form_data.target_user_name": name
                    }
                ]
            }
        elif entry_type == "computer":
            alert_query = {
                "domain": domain,
                "$or": [
                    {
                        "form_data.source_workstation": name
                    },
                    {
                        "dc_hostname": name
                    },
                    {
                        "form_data.dc_hostname": name
                    }
                ]
            }
        else:
            return 0
        activities_ids = self.alert.get_activity_ids_by_query(alert_query)
        return len(activities_ids)

    def related_list(self, data: dict) -> list:
        """
            查询实体相关威胁活动记录
        """
        if data["entry_type"] == "user":
            user_name = data["entry_name"]
            alert_query = {
                "domain": data["domain"],
                "$or": [
                    {
                        "form_data.source_user_name": user_name
                    },
                    {
                        "form_data.target_user_name": user_name
                    }
                ]
            }
        elif data["entry_type"] == "computer":
            computer_name = data["entry_name"]
            alert_query = {
                "domain": data["domain"],
                "$or": [
                    {
                        "form_data.source_workstation": computer_name
                    },
                    {
                        "dc_hostname": computer_name
                    },
                    {
                        "form_data.dc_hostname": computer_name
                    }
                ]
            }
        else:
            return []
        activities_ids = self.alert.get_activity_ids_by_query(alert_query)
        activity_query = {
            "_id": {
                "$in": activities_ids
            }
        }
        search = self.activity_mongo.find_all(activity_query)
        fetcher = search.sort("end_time", -1)

        result = []
        for each in fetcher:
            each["start_time"] = datetime_to_utc(each["start_time"])
            each["end_time"] = datetime_to_utc(each["end_time"])
            each["desc_data"] = self._get_desc_data(each["_id"], each["description"])
            result.append(each)
        return result

    def detail(self, _id) -> dict:
        activity_id = ObjectId(_id)
        query = {"_id": activity_id}

        result = self.activity_mongo.find_one(query)

        alerts = self.alert.list(activity_id)

        result["start_time"] = datetime_to_utc(result["start_time"])
        result["end_time"] = datetime_to_utc(result["end_time"])
        desc_data = self._get_desc_data(result["_id"], result["description"])
        result["desc_data"] = desc_data
        result["alert_list"] = alerts
        graph_data = self._get_desc_data(result["_id"], result["description"], only_name=True)
        result["graph"] = graph_map[result["alert_code"]](graph_data, second_name=result.get("second_name", None))
        return result

    def statistic_status_level(self) -> dict:
        """
            统计当前威胁活动各个分类的状态
        """
        result = {}
        aggs = [
            {
                "$group": {
                    "_id": "$status",
                    "count": {
                        "$sum": 1
                    }
                }
            }
        ]
        data = list(self.activity_mongo.aggregate(aggs))
        status_list = ["pending", "ignore", "auto_ignore", "mistake", "closed", "finished"]
        for status in status_list:
            for each in data:
                if status == each["_id"]:
                    result[each["_id"]] = {
                        "total": each["count"],
                        **self.statistic_level(each["_id"])
                    }
            if status not in result:
                result[status] = {
                    "total": 0,
                    "high": 0,
                    "medium": 0,
                    "low": 0
                }
        return result

    def statistic_level(self, status) -> dict:
        result = {}
        aggs = [
            {
                "$match": {
                    "status": status,
                }
            },
            {
                "$group": {
                    "_id": "$level",
                    "count": {
                        "$sum": 1
                    }
                }
            }
        ]
        data = self.activity_mongo.aggregate(aggs)
        for each in data:
            result[each["_id"]] = each["count"]
        level_list = ["high", "medium", "low"]
        for level in level_list:
            if level not in result:
                result[level] = 0
        return result

    def count(self, **kwargs) -> int:
        return self.activity_mongo.count(kwargs)

    def delete(self, _id):
        """
            删除某个威胁活动，包括所属的所有告警
        """
        self.activity_mongo.delete_one({
            "_id": ObjectId(_id)
        })
        self.alert.delete(ObjectId(_id))

    def ignore(self, _id):
        """
            忽略某个活动
        """
        query = {"_id": ObjectId(_id)}
        self.activity_mongo.update_one(filter=query, doc={
            "$set": {
                "status": "ignore"
            }
        })
        self.alert.ignore(activity_id=ObjectId(_id))

    def mistake(self, _id):
        """
            将某个活动设置为误报
        """
        query = {"_id": ObjectId(_id)}
        self.activity_mongo.update_one(filter=query, doc={
            "$set": {
                "status": "mistake"
            }
        })
        self.alert.mistake(activity_id=ObjectId(_id))

    def close(self, _id):
        """
            将某个活动设置为关闭
        """
        query = {"_id": ObjectId(_id)}
        self.activity_mongo.update_one(filter=query, doc={
            "$set": {
                "status": "closed"
            }
        })
        self.alert.close(activity_id=ObjectId(_id))

    def finish(self, _id):
        """
            将某个活动设置为关闭
        """
        query = {"_id": ObjectId(_id)}
        self.activity_mongo.update_one(filter=query, doc={
            "$set": {
                "status": "finished"
            }
        })
        self.alert.finish(activity_id=ObjectId(_id))

    def _get_desc_data(self, _id: ObjectId, desc: str, only_name=False) -> list:
        fields = re.findall(r"\[(.+?)]", desc)

        def _get_fields(_data) -> dict:
            _result = {}
            for each in _data:
                _result["form_data." + each] = True
            return _result

        data = self.alert.list(_id, fields=_get_fields(fields))

        result_dict = {}
        for one in data:
            for key, value in one["form_data"].items():
                if key not in result_dict:
                    result_dict[key] = []
                if isinstance(value, list):
                    result_dict[key].extend(value)
                else:
                    result_dict[key].append(value)

        def _add_other_info(field, value_list) -> list:
            _result = []
            value_list = list(set(value_list))

            if only_name:
                return value_list

            for _value in value_list:
                if _value is None:
                    _value = "unknown"
                _result.append({
                    "name": _value,
                    "type": _get_entry_type(field, _value)
                })

            return _result

        def _dict_to_order_list() -> list:
            _list = []
            for field in fields:
                _list.append({
                    "name": field,
                    "value": _add_other_info(field, result_dict[field])
                })
            return _list

        result_list = _dict_to_order_list()
        return result_list

    def get_filter_data(self, data: dict) -> dict:
        activity_query = {}
        alert_query = {}
        for key, value in data.items():
            if key == "showProgressBar":
                continue
            if not data[key] or data[key] == "" or len(data[key]) == 0:
                continue
            if key == "start_time":
                activity_query[key] = {
                    "$gte": utc_to_datetime(data[key])
                }
            elif key == "end_time":
                activity_query[key] = {
                    "$lte": utc_to_datetime(data[key])
                }

                # TODO
            elif key == "level":
                if data[key] == "all":
                    continue
                if isinstance(data[key], list):
                    activity_query[key] = {
                        "$in": data[key]
                    }
                else:
                    activity_query[key] = data[key]
            elif "filter" in key:
                continue
            elif key == "status" and data[key] == "all":
                continue
            else:
                activity_query[key] = data[key]
        if data["filter_value"] != "" and data["filter_name"] != "":
            alert_query["form_data." + data["filter_name"]] = data["filter_value"]
            activities_ids = self.alert.get_activity_ids_by_query(alert_query)
            activity_query["_id"] = {
                "$in": activities_ids
            }
        return activity_query

    def _count_by_custom(self, field: str, value: str) -> int:
        """
            根据自定义条件统计相关威胁活动数量
        """
        query = {
            field: value
        }
        return self.activity_mongo.count(query)


def _get_entry_type(field_name, value):
    if value and value.endswith("$"):
        return "computer"

    if "user" in field_name:
        return "user"
    elif "workstation" in field_name or "computer" in field_name or "hostname" in field_name:
        return "computer"
    elif "dc" in field_name:
        return "server"
    elif "group" in field_name:
        return "group"
    elif "ip" in field_name:
        return "ip"
    elif "service" in field_name:
        return "service"
    else:
        return "default"


if __name__ == '__main__':
    print(Activity().statistic_status_level())