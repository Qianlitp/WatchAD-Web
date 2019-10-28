#!/usr/bin/python3
# coding: utf-8

"""
    账户在域内的活动
"""

from flask import Blueprint, request
from application.common.common import output_json
from application.modules.Record import Record


record_blueprint = Blueprint(
    "record",
    __name__,
)


@record_blueprint.route("/record/list", methods=["POST"])
def get_list():
    """
        所有相关的活动
    """
    post_data = request.get_json()

    record = Record()
    result = record.list(data=post_data)

    return output_json({
        "errno": 0,
        "data": result
    })


@record_blueprint.route("/record/logon_ips", methods=["POST"])
def logon_ips():
    post_data = request.get_json()

    record = Record()

    result = record.logon_ips(data=post_data)
    return output_json({
        "errno": 0,
        "data": result
    })


@record_blueprint.route("/record/used_computers", methods=["POST"])
def used_computers():
    post_data = request.get_json()

    record = Record()

    result = record.used_computers(data=post_data)
    return output_json({
        "errno": 0,
        "data": result
    })


@record_blueprint.route("/record/logon_users", methods=["POST"])
def logon_users():
    post_data = request.get_json()

    record = Record()

    result = record.logon_users(data=post_data)
    return output_json({
        "errno": 0,
        "data": result
    })


@record_blueprint.route("/record/access_entries", methods=["POST"])
def access_entries():
    post_data = request.get_json()

    record = Record()

    result = record.access_entries(data=post_data)
    return output_json({
        "errno": 0,
        "data": result
    })
