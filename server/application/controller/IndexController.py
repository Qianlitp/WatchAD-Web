#!/usr/bin/python3
# coding: utf-8
from flask import Blueprint, request


index_blueprint = Blueprint(
    "index",
    __name__,
)


@index_blueprint.route("/index", methods=["GET"])
def index():
    return "ok"
