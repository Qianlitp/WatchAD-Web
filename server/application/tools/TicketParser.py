#!/usr/bin/python3
# coding: utf-8

from application.common.common import hex2bin_number


class TicketParser(object):
    def __init__(self):
        pass

    def option_parse(self, ticket_option):
        option_list = []

        bin_number = hex2bin_number(ticket_option).replace("b", "")
        for index, value in enumerate(bin_number):
            if value == "1" and int(index) in TicketOptionBitFLag:
                option_list.append(TicketOptionBitFLag[int(index)])
        return option_list

    def encryption_parse(self, encryption_type):
        encryption_type = encryption_type.lower()
        if encryption_type in EncryptionTypes:
            return EncryptionTypes[encryption_type]
        else:
            return None


TicketOptionBitFLag = {
    0: {
        "name": "Reserved",
        "description": "-"
    },
    1: {
        "name": "Forwardable",
        "description": "(TGT only). Tells the ticket-granting service that it can issue a new TGT—based on the presented TGT—with a different network address based on the presented TGT."
    },
    2: {
        "name": "Forwarded",
        "description": "Indicates either that a TGT has been forwarded or that a ticket was issued from a forwarded TGT."
    },
    3: {
        "name": "Proxiable",
        "description": "(TGT only). Tells the ticket-granting service that it can issue tickets with a network address that differs from the one in the TGT."
    },
    4: {
        "name": "Proxy",
        "description": "Indicates that the network address in the ticket is different from the one in the TGT used to obtain the ticket."
    },
    5: {
        "name": "Allow-postdate",
        "description": "Postdated tickets SHOULD NOT be supported in KILE (Microsoft Kerberos Protocol Extension)."
    },
    6: {
        "name": "Postdated",
        "description": "Postdated tickets SHOULD NOT be supported in KILE (Microsoft Kerberos Protocol Extension)."
    },
    7: {
        "name": "Invalid",
        "description": "This flag indicates that a ticket is invalid, and it must be validated by the KDC before use. Application servers must reject tickets which have this flag set."
    },
    8: {
        "name": "Renewable",
        "description": "Used in combination with the End Time and Renew Till fields to cause tickets with long life spans to be renewed at the KDC periodically."
    },
    9: {
        "name": "Initial",
        "description": "Indicates that a ticket was issued using the authentication service (AS) exchange and not issued based on a TGT."
    },
    10: {
        "name": "Pre-authent",
        "description": "Indicates that the client was authenticated by the KDC before a ticket was issued. This flag usually indicates the presence of an authenticator in the ticket. It can also flag the presence of credentials taken from a smart card logon."
    },
    11: {
        "name": "Opt-hardware-auth",
        "description": "This flag was originally intended to indicate that hardware-supported authentication was used during pre-authentication. This flag is no longer recommended in the Kerberos V5 protocol. KDCs MUST NOT issue a ticket with this flag set. KDCs SHOULD NOT preserve this flag if it is set by another KDC."
    },
    12: {
        "name": "Transited-policy-checked",
        "description": "KILE MUST NOT check for transited domains on servers or a KDC. Application servers MUST ignore the TRANSITED-POLICY-CHECKED flag."
    },
    13: {
        "name": "Ok-as-delegate",
        "description": "The KDC MUST set the OK-AS-DELEGATE flag if the service account is trusted for delegation."
    },
    14: {
        "name": "Request-anonymous",
        "description": "KILE not use this flag."
    },
    15: {
        "name": "Name-canonicalize",
        "description": "In order to request referrals the Kerberos client MUST explicitly request the \"canonicalize\" KDC option for the AS-REQ or TGS-REQ."
    },
    26: {
        "name": "Disable-transited-check",
        "description": "By default the KDC will check the transited field of a TGT against the policy of the local realm before it will issue derivative tickets based on the TGT. If this flag is set in the request, checking of the transited field is disabled. Tickets issued without the performance of this check will be noted by the reset (0) value of the TRANSITED-POLICY-CHECKED flag, indicating to the application server that the transited field must be checked locally. KDCs are encouraged but not required to honor the DISABLE-TRANSITED-CHECK option. Should not be in use, because Transited-policy-checked flag is not supported by KILE."
    },
    27: {
        "name": "Renewable-ok",
        "description": "The RENEWABLE-OK option indicates that a renewable ticket will be acceptable if a ticket with the requested life cannot otherwise be provided, in which case a renewable ticket may be issued with a renew-till equal to the requested end time. The value of the renew-till field may still be limited by local limits, or limits selected by the individual principal or server."
    },
    28: {
        "name": "Enc-tkt-in-skey",
        "description": "No information."
    },
    30: {
        "name": "Renew",
        "description": "The RENEW option indicates that the present request is for a renewal. The ticket provided is encrypted in the secret key for the server on which it is valid. This option will only be honored if the ticket to be renewed has its RENEWABLE flag set and if the time in it’s renew-till field has not passed. The ticket to be renewed is passed in the padata field as part of the authentication header."
    },
    31: {
        "name": "Validate",
        "description": "This option is used only by the ticket-granting service. The VALIDATE option indicates that the request is to validate a postdated ticket. Should not be in use, because postdated tickets are not supported by KILE."
    }
}


EncryptionTypes = {
    "0x1": "DES-CBC-CRC",
    "0x3": "DES-CBC-MD5",
    "0x11": "AES128-CTS-HMAC-SHA1-96",
    "0x12": "AES256-CTS-HMAC-SHA1-96",
    "0x17": "RC4-HMAC",
    "0x18": "RC4-HMAC-EXP"
}


PreAuthenticationTypes = {
    0: {
        "name": "-",
        "description": "Logon without Pre-Authentication."
    },
    2: {
        "name": "PA-ENC-TIMESTAMP",
        "description": "This is a normal type for standard password authentication."
    },
    11: {
        "name": "PA-ETYPE-INFO",
        "description": "The ETYPE-INFO pre-authentication type is sent by the KDC in a KRB-ERROR indicating a requirement for additional pre-authentication. It is usually used to notify a client of which key to use for the encryption of an encrypted timestamp for the purposes of sending a PA-ENC-TIMESTAMP pre-authentication value. Never saw this Pre-Authentication Type in Microsoft Active Directory environment."
    },
    15: {
        "name": "PA-PK-AS-REP_OLD",
        "description": "Used for Smart Card logon authentication."
    },
    17: {
        "name": "PA-PK-AS-REP",
        "description": "This type should also be used for Smart Card authentication, but in certain Active Directory environments, it is never seen."
    },
    19: {
        "name": "PA-ETYPE-INFO2",
        "description": "The ETYPE-INFO2 pre-authentication type is sent by the KDC in a KRB-ERROR indicating a requirement for additional pre-authentication. It is usually used to notify a client of which key to use for the encryption of an encrypted timestamp for the purposes of sending a PA-ENC-TIMESTAMP pre-authentication value. Never saw this Pre-Authentication Type in Microsoft Active Directory environment."
    },
    20: {
        "name": "PA-SVR-REFERRAL-INFO",
        "description": "Used in KDC Referrals tickets."
    },
    138: {
        "name": "PA-ENCRYPTED-CHALLENGE",
        "description": "Logon using Kerberos Armoring (FAST). Supported starting from Windows Server 2012 domain controllers and Windows 8 clients."
    },
}

if __name__ == '__main__':
    option = TicketParser().option_parse("0x40800010")
    print(option)
