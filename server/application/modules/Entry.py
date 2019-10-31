#!/usr/bin/python3
# coding: utf-8

import re
from impacket.ldap.ldaptypes import SR_SECURITY_DESCRIPTOR
from application.common.common import datetime_to_utc, get_cn_from_dn, get_netbios_domain, get_domain_from_dn, escape_ldap_filter
from application.tools.LDAPSearch import LDAPSearch
from database.ElsaticHelper import *
from application.tools.GroupTypeParser import GroupTypeParser
from config.config import main_config
from application.tools.UACFlagsParser import UACFlagsParser
from application.modules.Activity import Activity


class Entry(object):
    def __init__(self, domain):
        self.domain = get_netbios_domain(domain)
        self.ldap = LDAPSearch(domain)
        self.es = ElasticHelper()
        self.uac_parser = UACFlagsParser()
        self.group_type_parser = GroupTypeParser()

    def fuzz_search(self, name, page_size=5, **kwargs) -> list:
        result = []
        name = escape_ldap_filter(name)
        condition = "(&(cn=*{name}*)(|(objectClass=computer)(objectClass=user)(objectClass=group)))".format(name=name)
        entries = self.ldap.search_by_custom(condition, attributes=["cn", "distinguishedName", "userAccountControl",
                                                                "objectSid", "adminCount", "memberOf", "objectClass",
                                                                "description"],
                                                                paged_size=page_size)
        if not entries:
            return result
        for entry in entries:
            temp = {}
            entry_attributes = entry.entry_attributes_as_dict

            if "computer" in entry_attributes["objectClass"]:
                temp["entry_type"] = "computer"
            elif "group" in entry_attributes["objectClass"]:
                temp["entry_type"] = "group"
            elif "user" in entry_attributes["objectClass"]:
                temp["entry_type"] = "user"
            else:
                continue

            for key, value in entry_attributes.items():
                if key == "distinguishedName":
                    temp["domain"] = get_netbios_domain(get_domain_from_dn(value[0]))
                elif temp["entry_type"] != "group" and key == "userAccountControl":
                    temp["is_disabled"] = self.uac_parser.has_one_flag(value[0], "ACCOUNT_DISABLE")
                elif key == "objectSid":
                    # TODO 改为敏感组的判断方式
                    temp["is_sensitive"] = self.user_is_sensitive(value[0],
                                                                  admin_count=entry_attributes["adminCount"],
                                                                  member_of=entry_attributes["memberOf"])
                elif key == "cn":
                    temp["cn"] = value[0]
                elif key == "description" and len(value) > 0:
                    temp["description"] = value[0]

            temp["alert_count"] = Activity().related_count(temp["entry_type"], temp["domain"], temp["cn"])
            result.append(temp)
        return result

    def check_entry(self, entry_type, name):
        if entry_type == "computer":
            name += "$"
        entry = self.ldap.search_by_name(name, attributes=["objectSid", "objectClass"])
        if entry:
            if entry_type not in entry["objectClass"]:
                return None
            return str(entry["objectSid"])
        else:
            return None

    def user_entry_data(self, name):
        result = {
            "domain": self.domain,
            "name": name
        }
        fields = ["department", "displayName", "mail", "manager", "title", "whenCreated", "sAMAccountName",
                  "objectSid", "description", "employeeNumber", "cn", "userAccountControl", "memberOf", "adminCount"]
        entry = self.ldap.search_by_name(name, attributes=fields)
        if entry:
            entry_attributes = entry.entry_attributes_as_dict
            for key, value in entry_attributes.items():
                if len(value) == 0:
                    result[key] = ""
                    continue
                elif key == "adminCount" or key == "memberOf":
                    continue
                elif key == "whenCreated":
                    result[key] = datetime_to_utc(value[0])
                elif key == "manager":
                    m = get_cn_from_dn(value[0])
                    if m:
                        result[key] = m
                    else:
                        result[key] = ""
                elif key == "userAccountControl":
                    result["is_disabled"] = self.uac_parser.has_one_flag(value[0], "ACCOUNT_DISABLE")
                elif key == "objectSid":
                    result["objectSid"] = value[0]
                    result["is_sensitive"] = self.user_is_sensitive(value[0],
                                                                    admin_count=entry_attributes["adminCount"],
                                                                    member_of=entry_attributes["memberOf"])
                elif len(value) == 1:
                    result[key] = value[0]
                elif len(value) > 1:
                    result[key] = "、".join(value)
                else:
                    result[key] = ""
        return result

    def computer_entry_data(self, name):
        result = {}
        fields = ["operatingSystem", "operatingSystemServicePack", "operatingSystemVersion", "sAMAccountName",
                  "whenCreated", "cn", "objectSid", "lastLogonTimestamp", "distinguishedName", "adminCount"]
        if not name.endswith("$"):
            name = name + "$"
        entry = self.ldap.search_by_name(name, attributes=fields)
        if entry:
            entry_attributes = entry.entry_attributes_as_dict
            result["is_sensitive"] = self.computer_is_sensitive(name=entry_attributes["cn"][0],
                                                                domain=self.domain,
                                                                admin_count=entry_attributes["adminCount"])
            result["is_dc"] = True if name[:-1] in main_config.get_dc_name_list(get_netbios_domain(self.domain)) else False
            for key, value in entry.entry_attributes_as_dict.items():
                if key == "whenCreated" or key == "lastLogonTimestamp":
                    result[key] = datetime_to_utc(value[0])
                elif len(value) == 1:
                    result[key] = value[0]
                elif len(value) > 1:
                    result[key] = "、".join(value)
                else:
                    result[key] = ""
        return result

    def group_entry_data(self, name):
        result = {"domain": self.domain}
        fields = ["description", "adminCount", "groupType", "member", "whenCreated", "sAMAccountName", "managedBy",
                  "cn", "objectSid"]
        entry = self.ldap.search_by_name(name, attributes=fields)
        if entry:
            for key, value in entry.entry_attributes_as_dict.items():
                if key == "whenCreated" or key == "whenChanged":
                    result[key] = datetime_to_utc(value[0])
                elif key == "adminCount":
                    result["is_sensitive"] = self.group_is_sensitive(name, domain=self.domain, admin_count=value)
                elif key == "groupType":
                    result["scope"], result["type"] = self.group_type_parser.parse(value[0])
                elif key == "member":
                    result["member_count"] = len(value)
                elif key == "objectSid":
                    result["objectSid"] = value[0]
                elif key == "managedBy":
                    if len(value) > 0:
                        result["managedBy"] = get_cn_from_dn(value[0])
                    else:
                        result["managedBy"] = ""
                elif len(value) == 1:
                    result[key] = value[0]
                else:
                    result[key] = value
        return result

    def detail_user_data(self, name):
        result = {}
        fields = ["sAMAccountName", "objectSid", "userPrincipalName", "distinguishedName", "servicePrincipalName",
                  "whenCreated", "userAccountControl", "memberOf", "manager", "directReports",
                  "msDS-AllowedToDelegateTo", "cn"]
        entry = self.ldap.search_by_name(name, attributes=fields)
        if entry:
            for key, value in entry.entry_attributes_as_dict.items():
                if len(value) == 0:
                    result[key] = None
                    continue
                elif key == "whenCreated":
                    result[key] = datetime_to_utc(value[0])
                elif key == "manager":
                    m = get_cn_from_dn(value[0])
                    if m:
                        result[key] = self.user_entry_data(m)
                    else:
                        result[key] = ""
                elif key == "userAccountControl":
                    result[key] = self.uac_parser.parse_security(value[0])
                    result["is_disabled"] = self.uac_parser.has_one_flag(value[0], "ACCOUNT_DISABLE")
                elif key == "directReports":
                    result[key] = self._multi_entry_data(value)
                elif key == "memberOf":
                    result[key] = self._multi_entry_data(value)
                    result["recursive_groups"] = self._get_recursive_groups(value)
                elif key == "servicePrincipalName" or key == "msDS-AllowedToDelegateTo":
                    result[key] = value
                elif len(value) == 1:
                    result[key] = value[0]
                else:
                    result[key] = value
        return result

    def detail_group_data(self, name):
        result = {}
        fields = ["sAMAccountName", "objectSid", "distinguishedName", "whenCreated", "memberOf", "member", "cn"]
        entry = self.ldap.search_by_name(name, attributes=fields)
        if entry:
            for key, value in entry.entry_attributes_as_dict.items():
                if len(value) == 0:
                    result[key] = None
                    continue
                elif key == "whenCreated":
                    result[key] = datetime_to_utc(value[0])
                elif key == "member":
                    result[key] = self._multi_entry_data(value)
                elif key == "memberOf":
                    result[key] = self._multi_entry_data(value)
                elif len(value) == 1:
                    result[key] = value[0]
                else:
                    result[key] = value
            result["userAccountControl"] = self.uac_parser.parse_security(0)
        return result

    def detail_computer_data(self, name):
        result = {}
        fields = ["sAMAccountName", "objectSid", "distinguishedName", "whenCreated", "memberOf", "cn",
                  "userAccountControl", "dNSHostName", "servicePrincipalName",
                  "msDS-AllowedToActOnBehalfOfOtherIdentity"]
        if not name.endswith("$"):
            name += "$"
        entry = self.ldap.search_by_name(name, attributes=fields)
        if entry:
            for key, value in entry.entry_attributes_as_dict.items():
                if len(value) == 0:
                    result[key] = None
                    continue
                elif key == "whenCreated":
                    result[key] = datetime_to_utc(value[0])
                elif key == "memberOf":
                    result[key] = self._multi_entry_data(value)
                elif key == "userAccountControl":
                    result[key] = self.uac_parser.parse_security(value[0])
                elif key == "msDS-AllowedToActOnBehalfOfOtherIdentity":
                    sd = SR_SECURITY_DESCRIPTOR(value[0])
                    ace_list = []
                    for ace in sd["Dacl"].aces:
                        ace_list.append({
                            "type_name": ace["TypeName"],
                            "sid": ace['Ace']['Sid'].formatCanonical(),
                            "user_name": self.ldap.search_by_sid(sid=ace['Ace']['Sid'].formatCanonical(),
                                                                 attributes=["sAMAccountName"])
                                .entry_attributes_as_dict["sAMAccountName"][0]
                        })
                    result[key] = ace_list
                elif len(value) == 1:
                    result[key] = value[0]
                else:
                    result[key] = value
        return result

    def user_is_sensitive(self, sid, admin_count=None, member_of=None) -> bool:
        # 蜜罐账户
        for user in main_config.honeypot_user:
            if user["sid"] == sid:
                return True

        # 自定义敏感用户
        for user in main_config.sensitive_users:
            if user["sid"] == sid:
                return True

        if admin_count is None and member_of is None:
            ldap = LDAPSearch(self.domain)
            user_entry = ldap.search_by_sid(sid, attributes=["adminCount", "memberOf"])
            if not user_entry:
                return False
            admin_count = user_entry.entry_attributes_as_dict["adminCount"]
            member_of = user_entry.entry_attributes_as_dict["memberOf"]

        # adminCount
        if len(admin_count) > 0 and admin_count[0] == 1:
            return True

        # 敏感组
        groups = member_of
        for g in groups:
            g_name = get_cn_from_dn(g)
            g_domain = get_domain_from_dn(g)
            for g_entry in main_config.sensitive_groups:
                if g_entry["domain"] == g_domain and g_entry["name"] == g_name:
                    return True
        return False

    def group_is_sensitive(self, name, domain, admin_count) -> bool:
        if len(admin_count) > 0 and admin_count[0] == 1:
            return True

        # 敏感组
        for g_entry in main_config.sensitive_groups:
            if g_entry["domain"] == get_netbios_domain(domain) and g_entry["name"] == name:
                return True
        return False

    def computer_is_sensitive(self, name, domain, admin_count) -> bool:
        # DC
        if name.upper() in main_config.get_dc_name_list(get_netbios_domain(domain)):
            return True

        if len(admin_count) > 0 and admin_count[0] == 1:
            return True

        # 敏感组
        for computer in main_config.sensitive_computers:
            if computer["domain"] == get_netbios_domain(domain) and computer["name"] == name:
                return True
        return False

    def _multi_entry_data(self, entry_list) -> list:
        result = []
        if len(entry_list) == 0:
            return result
        condition = []
        for entry in entry_list:
            cn = get_cn_from_dn(entry)
            cn = escape_ldap_filter(cn)
            condition.append("(CN={cn})".format(cn=cn))
        if len(condition) >= 2:
            condition = "(|{cond})".format(cond="".join(condition))
        else:
            condition = condition[0]
        entries = self.ldap.search_by_custom(condition, attributes=["department", "displayName", "mail", "manager",
                                                                    "title", "whenCreated", "sAMAccountName", "objectSid",
                                                                    "description", "employeeNumber", "cn", "adminCount",
                                                                    "userAccountControl", "adminCount", "memberOf",
                                                                    "groupType", "member", "managedBy", "objectClass",
                                                                    "distinguishedName", "operatingSystem",
                                                                    "operatingSystemServicePack",
                                                                    "operatingSystemVersion"])
        if not entries:
            return result
        for entry in entries:
            temp = {"domain": self.domain}
            entry_attributes = entry.entry_attributes_as_dict

            if "computer" in entry_attributes["objectClass"]:
                temp["entry_type"] = "computer"
                temp["is_sensitive"] = self.computer_is_sensitive(name=entry_attributes["cn"][0],
                                                                  domain=self.domain,
                                                                  admin_count=entry_attributes["adminCount"])
            elif "group" in entry_attributes["objectClass"]:
                temp["entry_type"] = "group"
                temp["is_sensitive"] = self.group_is_sensitive(name=entry_attributes["cn"][0],
                                                               domain=self.domain,
                                                               admin_count=entry_attributes["adminCount"])
                temp["userAccountControl"] = self.uac_parser.parse_security(0)
            elif "user" in entry_attributes["objectClass"]:
                temp["entry_type"] = "user"
                temp["is_sensitive"] = self.user_is_sensitive(sid=entry_attributes["objectSid"][0],
                                                              admin_count=entry_attributes["adminCount"],
                                                              member_of=entry_attributes["memberOf"])
            else:
                continue

            for key, value in entry_attributes.items():
                if len(value) == 0:
                    temp[key] = ""
                    continue
                elif key == "adminCount" or key == "memberOf":
                    continue
                elif key == "whenCreated":
                    temp[key] = datetime_to_utc(value[0])
                elif key == "manager":
                    m = get_cn_from_dn(value[0])
                    if m:
                        temp[key] = m
                    else:
                        temp[key] = ""
                elif key == "userAccountControl":
                    temp["is_disabled"] = self.uac_parser.has_one_flag(value[0], "ACCOUNT_DISABLE")
                elif key == "groupType":
                    temp["scope"], temp["type"] = self.group_type_parser.parse(value[0])
                elif key == "member":
                    temp["member_count"] = len(value)
                elif key == "managedBy":
                    temp["managedBy"] = get_cn_from_dn(value[0])
                elif len(value) == 1:
                    temp[key] = value[0]
                elif len(value) > 1:
                    temp[key] = "、".join(value)
                else:
                    temp[key] = ""
            result.append(temp)
        return result

    def _get_recursive_groups(self, group_list) -> list:
        result = []
        group_result = []

        search_group = group_list

        recursive_count = 2
        while True:
            temp = []
            condition = ""
            for user in search_group:
                cn = get_cn_from_dn(user)
                cn = escape_ldap_filter(cn)
                condition += "(cn={cn})".format(cn=cn)
            condition = "(|{cond})".format(cond=condition)
            entries = self.ldap.search_by_custom(condition, attributes=["memberOf"])
            for entry in entries:
                for g in entry.entry_attributes_as_dict["memberOf"]:
                    if g in group_list or g in group_result or g in temp:
                        continue
                    temp.append(g)

            if len(temp) == 0:
                break

            temp_result = self._multi_entry_data(temp)
            for each in temp_result:
                each["recursive_count"] = recursive_count
                result.append(each)

            recursive_count += 1
            group_result.extend(temp)
        return result
