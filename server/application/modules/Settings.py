#!/usr/bin/python3
# coding: utf-8


import simplejson
from database.MongoHelper import MongoHelper
from database.RedisHelper import RedisHelper
from config.database_config import MongoConfig


class Settings(object):
    def __init__(self):
        self.settings_mongo = MongoHelper(MongoConfig.settings_collection)
        self.redis = RedisHelper()

    def get_setting(self, name):
        query = {
            "name": name
        }
        return self.settings_mongo.find_one(query)["value"]

    def set_setting(self, name, data):
        self.settings_mongo.update_one({
            "name": name
        }, {
            "$set": {
                "value": data
            }
        }, upsert=True)
        key = name + "_setting"
        if isinstance(data, list):
            if len(data) > 0 and isinstance(data[0], dict):
                self.redis.set_str_value(key, simplejson.dumps(data))
            else:
                self.redis.set_list(key, *data)
        elif isinstance(data, str):
            self.redis.set_str_value(key, data)
        elif isinstance(data, dict):
            self.redis.set_str_value(key, simplejson.dumps(data))
        elif isinstance(data, int):
            self.redis.set_str_value(key, str(data))


