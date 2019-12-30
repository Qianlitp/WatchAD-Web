#!/usr/bin/python3
# coding: utf-8

from datetime import datetime
import os
from database.MongoHelper import MongoHelper
from config.database_config import MongoConfig
basedir = os.path.abspath(os.path.dirname(__file__))


def str_to_datetime(utc_str):
    """
        字符串时间转化为datetime对象
    """
    return datetime.strptime(utc_str, "%Y-%m-%d %H:%M:%S")


class MainConfig(object):
    def __init__(self):
        self.db = MongoHelper(MongoConfig.settings_collection)

    @property
    def domain_list(self) -> list:
        return self.db.find_one({
            "name": "domain_list"
        })["value"]

    @property
    def dc_name_list(self) -> dict:
        return self.db.find_one({
            "name": "dc_name_list"
        })["value"]

    def get_dc_name_list(self, domain=None) -> list:
        return self.dc_name_list[domain]

    @property
    def sensitive_entry(self) -> dict:
        return self.db.find_one({
            "name": "sensitive_entry"
        })["value"]

    # 敏感计算机列表
    @property
    def sensitive_computers(self) -> list:
        return self.sensitive_entry["computer"]

    # 敏感的用户组
    @property
    def sensitive_groups(self) -> list:
        return self.sensitive_entry["group"]

    # 敏感的用户列表
    @property
    def sensitive_users(self) -> list:
        return self.sensitive_entry["user"]

    # 蜜罐用户列表
    @property
    def honeypot_user(self) -> list:
        return self.db.find_one({
            "name": "honeypot_account"
        })["value"]

    # ldap 查询需要的账号信息
    @property
    def ldap_account(self) -> dict:
        return self.db.find_one({
            "name": "ldap"
        })["value"]


main_config = MainConfig()


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ok yoo this is 0kee team'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
