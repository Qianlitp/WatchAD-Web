#!/usr/bin/python3
# coding: utf-8


GLOBAL_SCOPE = "Global"
DOMAIN_LOCAL_SCOPE = "DomainLocal"
UNIVERSAL_SCOPE = "Universal"
BUILTIN_SCOPE = "Builtin"

SECURITY_GROUP = "Security"
DISTRIBUTION_GROUP = "Distribution"


class GroupTypeParser(object):
    def __init__(self):
        pass

    def parse(self, flag: int) -> (str, str, ):
        """
            返回组类型
        """
        flag = int(flag)
        if flag < 0:
            security_or_distribution = SECURITY_GROUP
        else:
            security_or_distribution = DISTRIBUTION_GROUP

        if flag in [2, -2147483646]:
            scope = GLOBAL_SCOPE
        elif flag in [4, -2147483644]:
            scope = DOMAIN_LOCAL_SCOPE
        elif flag in [8, -2147483640]:
            scope = UNIVERSAL_SCOPE
        elif flag == -2147483643:
            scope = BUILTIN_SCOPE
        else:
            scope = ""
        return scope, security_or_distribution
