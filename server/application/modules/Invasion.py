#!/usr/bin/python3
# coding: utf-8


from database.MongoHelper import MongoHelper
from config.database_config import MongoConfig
from application.common.common import datetime_to_utc, utc_to_datetime
from application.modules.Activity import Activity
from bson.objectid import ObjectId


class Invasion(object):
    def __init__(self):
        self.invasion_mongo = MongoHelper(MongoConfig.invasions_collection)
        self.activity = Activity()

    def list(self, data: dict) -> list:
        query = {}
        search = self.invasion_mongo.find_all(query)
        page = data["page"]
        start = (page - 1) * 10
        fetcher = search.sort("end_time", -1).skip(start).limit(10)

        result = []
        for each in fetcher:
            each["start_time"] = datetime_to_utc(each["start_time"])
            each["end_time"] = datetime_to_utc(each["end_time"])
            each["activity_list"] = self.activity.list_naive(each["_id"])
            result.append(each)
        return result
