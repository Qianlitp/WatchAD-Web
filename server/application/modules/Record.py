#!/usr/bin/python3
# coding: utf-8

"""
    查询账户最近的活动记录
"""

from application.common.errors import NoSuchEntryType
from database.ElsaticHelper import *
from config.database_config import ElasticConfig
from config.config import main_config


class Record(object):
    def __init__(self):
        self.es = ElasticHelper()

    def list(self, data: dict) -> list:
        entry_type = data["entry_type"]
        entry_name = data["entry_name"]
        start_time = data["start_time"]
        activity_type = data["activity_type"]
        end_time = data["end_time"]
        page = data["page"]
        page_size = data["page_size"]
        query = {
            "query": self._get_search_body(entry_type, entry_name, start_time, end_time, activity_type),
            "from": (page - 1) * page_size,
            "size": page * page_size,
            "sort": {
                "@timestamp": "desc"
            }
        }
        rsp = self.es.search(body=query,
                             index=ElasticConfig.user_activity_index,
                             doc_type=ElasticConfig.user_activity_doc_type)
        if rsp:
            return list(map(lambda x: x["_source"], rsp["hits"]["hits"]))
        else:
            return []

    def logon_ips(self, data: dict) -> list:
        entry_type = data["entry_type"]
        entry_name = data["entry_name"]
        if entry_type == "computer" and not entry_name.endswith("$"):
            entry_name = entry_name + "$"
        query = {
            "query": get_must_statement(
                get_term_statement("event_id", 4624),
                get_term_statement("event_data.TargetUserName.keyword", entry_name)
            ),
            "size": 0,
            "aggs": get_aggs_statement("logon_ips", "terms", "event_data.IpAddress.keyword")
        }
        rsp = self.es.search(body=query, index=ElasticConfig.event_log_index, doc_type=ElasticConfig.event_log_doc_type)
        if rsp:
            result = []
            for each in rsp["aggregations"]["logon_ips"]["buckets"]:
                if each["key"] == "-" or each["key"] == "::1":
                    continue
                if each["key"] == "::ffff:127.0.0.1":
                    continue
                result.append(each["key"].replace("::ffff:", ""))
            return result
        else:
            return []

    def logon_users(self, data: dict) -> list:
        computer_name = data["entry_name"].upper()
        query = {
            "query": get_must_statement(
                get_term_statement("event_id", 4624),
                get_term_statement("event_data.WorkstationName.keyword", computer_name),
                get_must_not_statement(
                    get_wildcard_statement("event_data.TargetUserName.keyword", "*$")
                )
            ),
            "size": 0,
            "aggs": get_aggs_statement("logon_users", "terms", "event_data.TargetUserName.keyword")
        }
        rsp = self.es.search(body=query, index=ElasticConfig.event_log_index, doc_type=ElasticConfig.event_log_doc_type)
        if rsp:
            result = []
            for each in rsp["aggregations"]["logon_users"]["buckets"]:
                if each["key"] == "ANONYMOUS LOGON":
                    continue
                result.append(each["key"])
            return result
        else:
            return []

    def used_computers(self, data: dict) -> list:
        user_name = data["entry_name"]
        query = {
            "query": get_must_statement(
                get_should_statement(
                    get_term_statement("event_id", 4624),
                    get_must_statement(
                        get_term_statement("event_id", 4776),
                        get_term_statement("event_data.Status.keyword", "0x0"),
                    )
                ),
                get_term_statement("event_data.TargetUserName.keyword", user_name)
            ),
            "size": 0,
            "aggs": get_two_aggs_statement("used_computers_a", "terms", "event_data.WorkstationName.keyword",
                                           "used_computers_b", "terms", "event_data.Workstation.keyword")
        }
        rsp = self.es.search(body=query, index=ElasticConfig.event_log_index, doc_type=ElasticConfig.event_log_doc_type)
        if rsp:
            result = []
            buckets = rsp["aggregations"]["used_computers_a"]["buckets"] + rsp["aggregations"]["used_computers_b"]["buckets"]
            for each in buckets:
                if not each["key"] or each["key"] == "-" or each["key"].startswith("\\\\"):
                    continue
                if each["key"] in main_config.get_dc_name_list(data["domain"]):
                    continue
                result.append(each["key"])
            return list(set(result))
        else:
            return []

    def access_entries(self, data: dict) -> list:
        entry_name = data["entry_name"]
        entry_type = data["entry_type"]
        if entry_type == "computer":
            query = {
                "query": get_must_statement(
                    get_term_statement("activity_type", "access_entry"),
                    get_term_statement("data.source_workstation", entry_name),
                ),
                "size": 0,
                "aggs": get_aggs_statement("access_entry", "terms", "data.target_user_name.keyword")
            }
        elif entry_type == "user":
            query = {
                "query": get_must_statement(
                    get_term_statement("activity_type", "access_entry"),
                    get_term_statement("data.source_user_name", entry_name),
                ),
                "size": 0,
                "aggs": get_aggs_statement("access_entry", "terms", "data.target_user_name.keyword")
            }
        else:
            raise NoSuchEntryType()

        rsp = self.es.search(body=query, index=ElasticConfig.user_activity_index,
                             doc_type=ElasticConfig.user_activity_doc_type)
        if rsp:
            result = []
            for each in rsp["aggregations"]["access_entry"]["buckets"]:
                if each["key"].endswith("$"):
                    result.append({
                        "entry_name": each["key"][:-1],
                        "entry_type": "computer"
                    })
                else:
                    result.append({
                        "entry_name": each["key"],
                        "entry_type": "user"
                    })
            return result
        else:
            return []

    def _get_search_body(self, entry_type, entry_name, start_time=None, end_time=None, activity_type=None) -> dict:
        """
        根据实体类型和名称 生成对应的ES查询语句
        :param entry_type:
        :param entry_name:
        :return:
        """
        if entry_type == "user":
            query = get_should_statement(
                get_term_statement("user_name", entry_name),
                get_term_statement("data.target_user_name.keyword", entry_name),
                get_term_statement("data.source_user_name.keyword", entry_name)
            )
        elif entry_type == "computer":
            query = get_should_statement(
                get_term_statement("user_name", entry_name),
                get_term_statement("data.source_workstation.keyword", entry_name),
                get_term_statement("data.target_user_name.keyword", entry_name),
                get_term_statement("data.source_user_name.keyword", entry_name)
            )
        elif entry_type == "group":
            query = get_should_statement(
                get_term_statement("data.group_name.keyword", entry_name)
            )
        else:
            raise NoSuchEntryType()

        if start_time or end_time:
            query = get_must_statement(
                query,
                get_range_statement("@timestamp", start_time, end_time)
            )

        if activity_type:
            tmp = []
            for _type in activity_type:
                tmp.append(get_term_statement("activity_type", _type))
            if "must" in query["bool"]:
                query["bool"]["must"].append(
                    get_should_statement(*tmp)
                )
            else:
                query = get_must_statement(
                    query,
                    get_should_statement(*tmp)
                )
        return query
