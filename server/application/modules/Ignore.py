#!/usr/bin/python3
# coding: utf-8

"""
    忽略威胁活动

    可忽略本次 或 添加永久自动忽略规则
"""
from application.common.common import datetime_now_obj
from database.MongoHelper import MongoHelper
from config.database_config import MongoConfig


class Ignore(object):
    def __init__(self, alert_code):
        self.alert_code = alert_code
        self.ignore_mongo = MongoHelper(MongoConfig.ignore_collection)

    def add_ignore_rule(self, ignore_rules, comment="") -> bool:
        if not self._validate_ignore_rules(ignore_rules):
            return False

        self.ignore_mongo.insert_one({
            "alert_code": self.alert_code,
            "comment": comment,
            "rules": ignore_rules,
            "update_time": datetime_now_obj()
        })
        return True

    def _validate_ignore_rules(self, ignore_rules) -> bool:
        if not isinstance(ignore_rules, list):
            return False
        for rule in ignore_rules:
            for each in ["field_name", "field_type", "match_type", "value"]:
                if each not in rule:
                    return False

            if rule["field_type"] not in ["ip", "string", "list"]:
                return False

            if rule["match_type"] not in ["term", "regex", "ip"]:
                return False
        return True
