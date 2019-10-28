#!/usr/bin/python3
# coding: utf-8

from datetime import datetime
import simplejson
import os
from database.RedisHelper import RedisHelper
basedir = os.path.abspath(os.path.dirname(__file__))


class _GetConfig(object):
    def __init__(self):
        self.redis = RedisHelper()

    def get_str(self, key) -> str:
        return self.redis.get_str_value(key)

    def get_int(self, key) -> int:
        return int(self.redis.get_str_value(key))

    def get_dict(self, key) -> dict:
        return simplejson.loads(self.redis.get_str_value(key))

    def get_list(self, key) -> list:
        return self.redis.get_all_list(key)


config_redis = _GetConfig()


def str_to_datetime(utc_str):
    """
        字符串时间转化为datetime对象
    """
    return datetime.strptime(utc_str, "%Y-%m-%d %H:%M:%S")


class MainConfig(object):

    def __init__(self):
        pass


    # 需要分析的FQDN域名称列表
    @property
    def domain_list(self) -> list:
        return config_redis.get_list("domain_list_setting")

    # 域控计算机名列表
    @property
    def dc_name_list(self) -> dict:
        return config_redis.get_dict("dc_name_list_setting")

    def get_dc_name_list(self, domain=None) -> list:
        return config_redis.get_dict("dc_name_list_setting")[domain]

    def sensitive_entry(self) -> dict:
        s = config_redis.get_str("sensitive_entry_setting")
        return simplejson.loads(s)

    # 敏感计算机列表
    @property
    def sensitive_computers(self) -> list:
        return self.sensitive_entry()["computer"]

    # 敏感的用户组
    @property
    def sensitive_groups(self) -> list:
        return self.sensitive_entry()["group"]

    # 敏感的用户列表
    @property
    def sensitive_users(self) -> list:
        return self.sensitive_entry()["user"]

    # 蜜罐用户列表
    @property
    def honeypot_user(self) -> list:
        user_list = config_redis.get_list("honeypot_user_setting")
        return list(map(lambda x: simplejson.loads(x), user_list))

    # ldap 查询需要的账号信息
    @property
    def ldap_account(self) -> dict:
        return config_redis.get_dict("ldap_setting")


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
