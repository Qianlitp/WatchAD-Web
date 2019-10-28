#!/usr/bin/python3
# coding: utf-8

from elasticsearch5 import Elasticsearch, helpers
from config.database_config import ElasticConfig


class ElasticHelper(object):
    def __init__(self):
        self.es = Elasticsearch(ElasticConfig.uri)

    def index(self, body, index, doc_type):
        self.es.index(body=body, index=index, doc_type=doc_type)

    def bulk(self, body, index, doc_type):
        self.es.bulk(body=body, index=index, doc_type=doc_type)

    def scan(self, body, index, doc_type):
        return helpers.scan(self.es, query=body, index=index, doc_type=doc_type, preserve_order=True)

    def search(self, body, index, doc_type):
        try:
            rsp = self.es.search(body=body, index=index, doc_type=doc_type, request_timeout=100)
            if rsp.get("errors"):
                print("es search error")
                return
            return rsp
        except Exception as e:
            print("es search error: " + str(e))

    def count(self, body, index, doc_type):
        return self.es.count(index=index, doc_type=doc_type, body=body, request_timeout=100)

    def delete_index(self, index):
        return self.es.indices.delete(index=index)


def get_range_statement(field, gte_time, lte_time):
    return {
        "constant_score": {
            "filter": {
                "range": {
                    field: {
                        "gte": gte_time if gte_time else "now-1y",
                        "lte": lte_time if lte_time else "now"
                    }
                }
            }
        }
    }


def get_term_statement(field_name, value):
    return {
        "constant_score": {
            "filter": {
                "term": {
                    field_name: value
                }
            }
        }
    }


def get_must_statement(*args):
    return {
        "bool": {
            "must": [*args]
        }
    }


def get_should_statement(*args):
    return {
        "bool": {
            "should": [*args]
        }
    }


def get_terms_statement(field_name, value):
    return {
        "constant_score": {
            "filter": {
                "terms": {
                    field_name: value
                }
            }
        }
    }


def get_must_not_statement(statement):
    return {
        "bool": {
            "must_not": statement
        }
    }


def get_sort_statement(field, order):
    return {
        field: order
    }


def get_aggs_statement(name, aggs_type, field):
    return {
        name: {
            aggs_type: {
                "field": field,
                "size": 1000000
            }
        }
    }


def get_two_aggs_statement(name_a, aggs_type_a, field_a, name_b, aggs_type_b, field_b):
    return {
        name_a: {
            aggs_type_a: {
                "field": field_a,
                "size": 1000000
            }
        },
        name_b: {
            aggs_type_b: {
                "field": field_b,
                "size": 1000000
            }
        }
    }


def get_double_aggs_statement(name1, aggs_type1, field1, name2, aggs_type2, field2):
    return {
        name1: {
            aggs_type1: {
                "field": field1,
                "size": 1000000
            },
            "aggs": {
                name2: {
                    aggs_type2: {
                        "field": field2,
                        "size": 1000000
                    }
                }
            }
        }
    }


def get_wildcard_statement(field, value):
    return {
        "constant_score": {
            "filter": {
                "wildcard": {
                    field: value
                }
            }
        }
    }


def get_match_must_all(field, value):
    """
        match 查询，对于 text 字段分词忽略大小写
    """
    return {
        "constant_score": {
            "filter": {
                "match": {
                    field: {
                        "query": value,
                        "operator": "and"
                    }
                }
            }
        }
    }