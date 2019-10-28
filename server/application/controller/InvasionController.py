#!/usr/bin/python3
# coding: utf-8

"""
    入侵事件
"""

from flask import Blueprint, request
from application.common.common import output_json
from application.modules.Invasion import Invasion


invasion_blueprint = Blueprint(
    "invasion",
    __name__,
)


@invasion_blueprint.route("/invasion/list", methods=["POST"])
def get_list():
    post_data = request.get_json()
    invasion = Invasion()
    result = invasion.list(data=post_data)

    return output_json({
        "errno": 0,
        "data": result
    })
