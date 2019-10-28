#!/usr/bin/python3
# coding: utf-8

"""
    误报处理

    按照不同的告警种类 有不同的处理方式
"""
from config.database_config import MongoConfig
from application.common.common import datetime_now_obj
from database.RedisHelper import RedisHelper
from database.MongoHelper import MongoHelper


class Mistake(object):
    def __init__(self, alert_code):
        self.alert_code = alert_code
        self.redis = RedisHelper()
        self.exclude_mongo = MongoHelper(MongoConfig.exclude_collection)

    def exclude(self, field, value, **kwargs):
        """
        """
        self.add_exclude_rule(field, value, kwargs.get("comment", ""))

    def add_exclude_rule(self, field, value, comment=""):
        """
            创建误报规则
        """
        self.exclude_mongo.insert_one({
            "alert_code": self.alert_code,
            "comment": comment,
            "rules": [
                {
                    "field_name": field,
                    "field_type": "string",
                    "match_type": "term",
                    "value": value
                }
            ],
            "update_time": datetime_now_obj()
        })
