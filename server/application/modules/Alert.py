#!/usr/bin/python3
# coding: utf-8


from database.MongoHelper import MongoHelper
from config.database_config import MongoConfig
from bson.objectid import ObjectId
from application.common.common import datetime_to_utc


class Alert(object):
    def __init__(self):
        self.alert_mongo = MongoHelper(MongoConfig.alerts_collection)

    def delete(self, activity_id: ObjectId):
        self.alert_mongo.delete_many({
            "activity_id": activity_id
        })

    def list(self, activity_id: ObjectId, fields=None) -> list:
        result = []
        fetcher = self.alert_mongo.find_all(query={
            "activity_id": activity_id
        }, fields=fields)
        for each in fetcher:
            if "start_time" in each:
                each["start_time"] = datetime_to_utc(each["start_time"])
            if "end_time" in each:
                each["end_time"] = datetime_to_utc(each["end_time"])
            result.append(each)
        return result

    def get_activity_ids_by_query(self, query):
        result = []
        data = self.alert_mongo.find_all(query, fields={"activity_id": True})
        for each in data:
            result.append(each["activity_id"])
        return list(set(result))

    def mistake(self, activity_id):
        self.alert_mongo.update_one({
            "activity_id": activity_id
        }, {
            "$set": {
                "status": "mistake"
            }
        })

    def ignore(self, activity_id):
        self.alert_mongo.update_one({
            "activity_id": activity_id
        }, {
            "$set": {
                "status": "ignore"
            }
        })

    def close(self, activity_id):
        self.alert_mongo.update_one({
            "activity_id": activity_id
        }, {
            "$set": {
                "status": "closed"
            }
        })

    def finish(self, activity_id):
        self.alert_mongo.update_one({
            "activity_id": activity_id
        }, {
            "$set": {
                "status": "finished"
            }
        })

