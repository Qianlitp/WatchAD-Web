#!/usr/bin/python3
# coding: utf-8


class SecBaseException(Exception):
    def __init__(self, msg):
        self.msg = "[error] " + msg

    def __str__(self):
        return self.msg


class LDAPSearchFailException(SecBaseException):
    def __init__(self, msg=u"LDAP search fail"):
        SecBaseException.__init__(self, msg)


class MsearchException(SecBaseException):
    def __init__(self, msg=u"es msearch error"):
        SecBaseException.__init__(self, msg)


class NoSuchEntryType(SecBaseException):
    def __init__(self, msg=u"no such entry type"):
        SecBaseException.__init__(self, msg)
