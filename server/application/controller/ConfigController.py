#!/usr/bin/python3
# coding: utf-8

"""
    配置信息相关
"""

from flask import Blueprint
from application.common.common import output_json
from application.modules.Config import alert_map


config_blueprint = Blueprint(
    "config",
    __name__,
)


@config_blueprint.route("/config/types", methods=["GET"])
def get_list():
    result = []
    for classify_name, value in alert_map.items():
        children = []
        for code, name in value.items():
            children.append({
                "label": name,
                "value": code
            })
        result.append({
            "label": classify_name,
            "value": classify_name,
            "children": children
        })

    return output_json({
        "errno": 0,
        "data": result
    })
