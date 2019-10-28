#!/usr/bin/python3
# coding: utf-8

from bson import ObjectId
from application.common.common import datetime_now_obj, datetime_to_utc
from config.database_config import MongoConfig
from database.MongoHelper import MongoHelper
from application.modules.Config import get_title_by_code


class Exclusion(object):
    def __init__(self):
        self.exclude_mongo = MongoHelper(MongoConfig.exclude_collection)

    def list(self) -> list:
        result = []
        fetcher = self.exclude_mongo.find_all({})
        for rule in fetcher:
            rule["_id"] = str(rule["_id"])
            rule["add_time"] = datetime_to_utc(rule["add_time"])
            rule["update_time"] = datetime_to_utc(rule["update_time"])
            result.append(rule)
        return result

    def add(self, data):
        """
            创建误报规则
        """
        self.exclude_mongo.insert_one({
            "title": get_title_by_code(data["alert_code"]),
            "alert_code": data["alert_code"],
            "comment": data["comment"],
            "rules": data["rules"],
            "add_time": datetime_now_obj(),
            "update_time": datetime_now_obj()
        })

    def delete(self, _id):
        self.exclude_mongo.delete_one({"_id": ObjectId(_id)})

    def update(self, data):
        self.exclude_mongo.update_one({
            "_id": ObjectId(data["id"])
        }, {
            "$set": data["data"]
        })
