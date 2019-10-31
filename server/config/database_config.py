#!/usr/bin/python3
# coding: utf-8


class ElasticConfig(object):
    host = "127.0.0.1:9200"
    uri = "http://{host}/".format(host=host)

    # -----------下方名称默认即可-------------
    event_log_index = "dc_log_all"
    event_log_doc_type = "security_log"
    traffic_index = "dc_traffic_all"
    traffic_krb_doc_type = "kerberos"
    user_activity_index = "user_activity_all"
    user_activity_doc_type = "user_activity"
    krb5_ticket_index = "krb5_ticket_all"
    krb5_ticket_doc_type = "ticket"
    # --------------------------------------


class MongoConfig(object):
    host = "127.0.0.1:27017"
    user = "WatchAD"
    password = "WatchAD-by-0KEE"
    uri = "mongodb://{user}:{password}@{host}/".format(host=host, user=user, password=password)

    # -----------下方名称默认即可-------------

    db = "WatchAD"
    delay_run_collection = "ad_delay"
    settings_collection = "ad_settings"
    delegation_collection = "ad_delegation"
    learning_collection = "ad_learning"
    alerts_collection = "ad_alerts"
    activities_collection = "ad_activities"
    invasions_collection = "ad_invasions"
    exclude_collection = "ad_exclusions"
    ignore_collection = "ad_ignore"
    # --------------------------------------


class RedisConfig(object):
    host = "127.0.0.1"
    port = 6379
