#!/usr/bin/python3
# coding: utf-8

from pymongo import MongoClient
from config.database_config import MongoConfig


class MongoHelper(object):
    def __init__(self, collection):
        uri = MongoConfig.uri
        db = MongoConfig.db
        self.client = MongoClient(uri, connect=False)
        self.db = self.client[db]
        self.handle = self.db[collection]

    def get_handle(self):
        return self.handle

    def find_all(self, query: dict, fields=None, **condition):
        body = dict(query, **condition)
        if fields:
            return self.handle.find(body, fields)
        else:
            return self.handle.find(body)

    def find_one(self, query: dict, **condition):
        body = dict(query, **condition)
        return self.handle.find_one(body)

    def insert_one(self, doc: dict, **condition):
        return self.handle.insert_one(doc, **condition)

    def insert_many(self, docs: list, **condition):
        self.handle.insert_many(docs, **condition)

    def replace_one(self, filter: dict, doc: dict, upsert: bool, **condition):
        self.handle.replace_one(filter, doc, upsert, **condition)

    def update_one(self, filter: dict, doc: dict, upsert=False):
        self.handle.update_one(filter, doc, upsert=upsert)

    def delete_one(self, filter: dict):
        self.handle.delete_one(filter)

    def delete_many(self, filter: dict):
        self.handle.delete_many(filter)

    def aggregate(self, aggs: list):
        return self.handle.aggregate(aggs)

    def count(self, query: dict):
        return self.handle.count(query)
