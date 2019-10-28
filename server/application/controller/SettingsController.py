#!/usr/bin/python3
# coding: utf-8


"""
    设置
"""

from ldap3 import Server, Connection, ALL
from flask import Blueprint, request
from application.common.common import output_success, output_error
from application.modules.Settings import Settings
from application.modules.Exclusion import Exclusion


setting_blueprint = Blueprint(
    "setting",
    __name__,
)


@setting_blueprint.route("/setting/<name>", methods=["GET", "POST"])
def setting(name):
    if request.method == "GET":
        result = Settings().get_setting(name)
        return output_success(result)
    elif request.method == "POST":
        post_data = request.get_json()
        Settings().set_setting(name, post_data["value"])
        return output_success("ok")


@setting_blueprint.route("/test_setting/test_ldap_con", methods=["POST"])
def test_ldap_con():
    post_data = request.get_json()
    setting = post_data["setting"]
    domain = list(setting.keys())[0]
    server = Server(setting[domain]["server"], get_info=ALL)
    try:
        con = Connection(server, user=setting[domain]["user"], password=setting[domain]["password"], auto_bind=True)
        return output_success("ok")
    except Exception as e:
        return output_error(2, str(e)), 500


@setting_blueprint.route("/setting/exclusion", methods=["GET", "POST", "PUT"])
def exclusion():
    exc = Exclusion()
    if request.method == "GET":
        result = exc.list()
        return output_success(result)
    elif request.method == "PUT":
        data = request.get_json()
        exc.add(data)
        result = exc.list()
        return output_success(result)
    elif request.method == "POST":
        data = request.get_json()
        exc.update(data)
        result = exc.list()
        return output_success(result)


@setting_blueprint.route("/setting/exclusion/delete/<_id>", methods=["DELETE"])
def delete_exclusion(_id):
    exc = Exclusion()
    exc.delete(_id)
    result = exc.list()
    return output_success(result)
