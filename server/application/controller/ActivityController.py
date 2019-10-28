#!/usr/bin/python3
# coding: utf-8

"""
    威胁活动的列表、详情、处理等
"""

from flask import Blueprint, request
from application.common.common import output_json
from application.modules.Activity import Activity
from application.modules.Mistake import Mistake
from application.modules.Ignore import Ignore


activity_blueprint = Blueprint(
    "activity",
    __name__,
)


@activity_blueprint.route("/activity/statistic", methods=["GET"])
def statistic():
    result = {}
    activity = Activity()
    data = activity.statistic_status_level()
    result["total"] = activity.count()
    result["data"] = data
    return output_json({
        "errno": 0,
        "data": result
    })


@activity_blueprint.route("/activity/list", methods=["POST"])
def get_list():
    post_data = request.get_json()
    activity = Activity()
    result = activity.list(data=post_data)

    return output_json({
        "errno": 0,
        "data": result
    })


@activity_blueprint.route("/activity/related_list", methods=["POST"])
def related_list():
    post_data = request.get_json()
    activity = Activity()
    result = activity.related_list(data=post_data)

    return output_json({
        "errno": 0,
        "data": result
    })


@activity_blueprint.route("/activity/<activity_id>", methods=["GET"])
def detail(activity_id):
    activity = Activity()
    result = activity.detail(_id=activity_id)

    return output_json({
        "errno": 0,
        "data": result
    })


@activity_blueprint.route("/activity/<activity_id>", methods=["DELETE"])
def delete(activity_id):
    activity = Activity()
    result = activity.delete(activity_id)
    return output_json({
        "errno": 0,
        "data": result
    })


@activity_blueprint.route("/activity/ignore", methods=["POST"])
def ignore():
    post_data = request.get_json()

    ignore_type = post_data["ignore_type"]

    activity = Activity()
    activity.ignore(post_data["id"])

    if ignore_type == "add_rule":
        i = Ignore(post_data["alert_code"])
        result = i.add_ignore_rule(post_data["rules"])
        if not result:
            return output_json({
                "errno": 1,
                "error": "规则格式或内容有误"
            })

    return output_json({
        "errno": 0,
        "data": ""
    })


@activity_blueprint.route("/activity/mistake", methods=["POST"])
def mistake():
    post_data = request.get_json()
    # 将某个活动标记为误报
    activity = Activity()
    activity.mistake(post_data["id"])

    # 设置规则，之后自动排除该类误报
    # m = Mistake(post_data["alert_code"])
    # m.exclude(**post_data)

    return output_json({
        "errno": 0,
        "data": ""
    })


@activity_blueprint.route("/activity/close", methods=["POST"])
def close():
    post_data = request.get_json()
    activity = Activity()
    activity.close(post_data["id"])

    return output_json({
        "errno": 0,
        "data": ""
    })


@activity_blueprint.route("/activity/finish", methods=["POST"])
def finish():
    post_data = request.get_json()
    activity = Activity()
    activity.finish(post_data["id"])

    return output_json({
        "errno": 0,
        "data": ""
    })
