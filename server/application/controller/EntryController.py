#!/usr/bin/python3
# coding: utf-8
"""
    域内实体信息相关
"""

from flask import Blueprint, request
from application.modules.Entry import Entry
from application.common.common import output_json, output_success, output_error
from config.config import main_config

entry_blueprint = Blueprint(
    "entry",
    __name__,
)


@entry_blueprint.route("/entry/fuzz_search", methods=["POST"])
def fuzz_search():
    post_data = request.get_json()
    result = []
    for domain in main_config.domain_list:
        entry = Entry(domain)
        entries = entry.fuzz_search(**post_data)
        result.extend(entries)
    return output_json({
        "errno": 0,
        "data": result
    })


@entry_blueprint.route("/entry/check_entry/<entry_type>/<domain>/<name>", methods=["GET"])
def check_entry(entry_type, domain, name):
    entry = Entry(domain)
    result = entry.check_entry(entry_type, name)
    if result:
        return output_success(result)
    else:
        return output_error(1, "no such entry"), 404


@entry_blueprint.route("/entry/user/<domain>/<name>", methods=["GET"])
def user(domain, name):
    entry = Entry(domain)
    result = entry.user_entry_data(name)
    return output_json({
        "errno": 0,
        "data": result
    })


@entry_blueprint.route("/entry/detail_user/<domain>/<name>", methods=["GET"])
def detail_user(domain, name):
    entry = Entry(domain)
    result = entry.detail_user_data(name)
    return output_json({
        "errno": 0,
        "data": result
    })


@entry_blueprint.route("/entry/detail_group/<domain>/<name>", methods=["GET"])
def detail_group(domain, name):
    entry = Entry(domain)
    result = entry.detail_group_data(name)
    return output_json({
        "errno": 0,
        "data": result
    })


@entry_blueprint.route("/entry/detail_computer/<domain>/<name>", methods=["GET"])
def detail_computer(domain, name):
    entry = Entry(domain)
    result = entry.detail_computer_data(name)
    return output_json({
        "errno": 0,
        "data": result
    })


@entry_blueprint.route("/entry/computer/<domain>/<name>", methods=["GET"])
def computer(domain, name):
    entry = Entry(domain)
    result = entry.computer_entry_data(name)
    return output_json({
        "errno": 0,
        "data": result
    })


@entry_blueprint.route("/entry/group/<domain>/<name>", methods=["GET"])
def group(domain, name):
    entry = Entry(domain)
    result = entry.group_entry_data(name)
    return output_json({
        "errno": 0,
        "data": result
    })
