#!/usr/bin/python3
# coding: utf-8


def _101(desc_data, **kwargs):
    return [
        _get_graph("icon-computer", desc_data[0]["value"], second_text=desc_data[1]["value"]),
        _get_arrow_graph("使用身份"),
        _get_graph("icon-secret", desc_data[2]["value"]),
        _get_arrow_graph("SAMR查询"),
        _get_graph("icon-group", desc_data[3]["value"])
    ]


def _102(desc_data, **kwargs):
    return [
        _get_graph("icon-computer", desc_data[0]["value"], second_text=desc_data[1]["value"]),
        _get_arrow_graph("使用身份"),
        _get_graph("icon-secret", desc_data[2]["value"]),
        _get_arrow_graph("SAMR查询"),
        _get_graph("icon-user", desc_data[3]["value"]),
    ]


def _103(desc_data, second_name):
    return [
        _get_graph("icon-computer", desc_data[0]["value"], second_text=desc_data[1]["value"]),
        _get_arrow_graph("使用身份"),
        _get_graph("icon-secret", desc_data[2]["value"]),
        _get_arrow_graph("PsLoggedOn"),
        _get_graph("icon-server", desc_data[3]["value"]),
    ]


def _104(desc_data, second_name):
    return [
        _get_graph("icon-computer", desc_data[0]["value"], second_text=desc_data[1]["value"]),
        _get_arrow_graph("访问蜜罐账户"),
        _get_graph("icon-user", desc_data[2]["value"])
    ]


def _201(desc_data, **kwargs):
    return [
        _get_graph("icon-computer", desc_data[0]["value"], second_text=desc_data[1]["value"]),
        _get_arrow_graph("请求目标"),
        _get_graph("icon-user", desc_data[2]["value"]),
        _get_arrow_graph("所属的服务票据"),
        _get_graph("icon-ticket", desc_data[3]["value"])
    ]


def _202(desc_data, **kwargs):
    return [
        _get_graph("icon-computer", desc_data[1]["value"], second_text=desc_data[2]["value"]),
        _get_arrow_graph("请求无需kerberos预认证目标", 300),
        _get_graph("icon-user", desc_data[0]["value"]),
        _get_arrow_graph("所属的TGT"),
        _get_graph("icon-ticket", ["弱加密票据"])
    ]


def _203(desc_data, **kwargs):
    return [
        _get_graph("icon-computer", desc_data[0]["value"], second_text=desc_data[1]["value"]),
        _get_arrow_graph("使用身份"),
        _get_graph("icon-secret", desc_data[2]["value"]),
        _get_arrow_graph("窃取域控NTDS.dit"),
        _get_graph("icon-server", desc_data[3]["value"])
    ]


def _301(desc_data, **kwargs):
    return [
        _get_graph("icon-computer", desc_data[0]["value"], second_text=desc_data[1]["value"]),
        _get_arrow_graph("暴力破解"),
        _get_graph("icon-ServiceGroup", ["多个账户"])
    ]


def _302(desc_data, **kwargs):
    return [
        _get_graph("icon-computer", desc_data[0]["value"], second_text=desc_data[1]["value"]),
        _get_arrow_graph("使用显式凭据远程登录目标", 300),
        _get_graph("icon-server", desc_data[2]["value"])
    ]


def _303(desc_data, **kwargs):
    return [
        _get_graph("icon-computer", desc_data[0]["value"], second_text=desc_data[1]["value"]),
        _get_arrow_graph("使用身份"),
        _get_graph("icon-secret", desc_data[2]["value"]),
        _get_arrow_graph("远程执行代码"),
        _get_graph("icon-server", desc_data[3]["value"])
    ]


def _304(desc_data, **kwargs):
    return [
        _get_graph("icon-computer", desc_data[0]["value"], second_text=desc_data[1]["value"]),
        _get_arrow_graph("使用身份"),
        _get_graph("icon-secret", desc_data[2]["value"]),
        _get_arrow_graph("访问了域控"),
        _get_graph("icon-server", desc_data[3]["value"]),
        _get_arrow_graph("所属未知文件共享"),
        _get_graph("icon-file", desc_data[4]["value"])
    ]


def _305(desc_data, **kwargs):
    return [
        _get_graph("icon-computer", desc_data[0]["value"], second_text=desc_data[1]["value"]),
        _get_arrow_graph("请求"),
        _get_graph("icon-user", desc_data[2]["value"]),
        _get_arrow_graph("所属的"),
        _get_graph("icon-ticket", ["弱加密票据"])
    ]


def _306(desc_data, **kwargs):
    return [
        _get_graph("icon-computer", desc_data[0]["value"], second_text=desc_data[1]["value"]),
        _get_arrow_graph("请求"),
        _get_graph("icon-user", desc_data[2]["value"]),
        _get_arrow_graph("所属的"),
        _get_graph("icon-ticket", ["异常内容票据"])
    ]


def _401(desc_data, **kwargs):
    return [
        _get_graph("icon-computer", desc_data[0]["value"], second_text=desc_data[1]["value"]),
        _get_arrow_graph("使用身份"),
        _get_graph("icon-secret", desc_data[2]["value"]),
        _get_arrow_graph("修改"),
        _get_graph("icon-settings", ["DACL"])
    ]


def _402(desc_data, **kwargs):
    return [
        _get_graph("icon-computer", desc_data[0]["value"], second_text=desc_data[1]["value"]),
        _get_arrow_graph("认证账户"),
        _get_graph("icon-secret", desc_data[2]["value"])
    ]


def _403(desc_data, **kwargs):
    return [
        _get_graph("icon-computer", desc_data[0]["value"], second_text=desc_data[1]["value"]),
        _get_arrow_graph("使用MS17-010 EXP攻击域控", 200),
        _get_graph("icon-server", desc_data[2]["value"])
    ]


def _404(desc_data, **kwargs):
    return [
        _get_graph("icon-computer", desc_data[0]["value"], second_text=desc_data[1]["value"]),
        _get_arrow_graph("使用身份"),
        _get_graph("icon-user", desc_data[2]["value"]),
        _get_arrow_graph("创建了新的"),
        _get_graph("icon-settings", ["组策略"])
    ]


def _405(desc_data, **kwargs):
    return [
        _get_graph("icon-computer", desc_data[0]["value"]),
        _get_arrow_graph("发出认证请求"),
        _get_graph("icon-computer", desc_data[1]["value"], second_text=desc_data[2]["value"]),
        _get_arrow_graph("将其中继到"),
        _get_graph("icon-server", desc_data[3]["value"]),
        _get_arrow_graph("获取目标身份特权", 150),
        _get_graph("icon-user", desc_data[4]["value"])
    ]


def _406(desc_data, **kwargs):
    return [
        _get_graph("icon-computer", desc_data[0]["value"], second_text=desc_data[1]["value"]),
        _get_arrow_graph("使用身份"),
        _get_graph("icon-secret", desc_data[2]["value"]),
        _get_arrow_graph("添加基于资源约束委派", 200),
        _get_graph("icon-computer", desc_data[3]["value"]),
    ]


def _407(desc_data, **kwargs):
    return [
        _get_graph("icon-computer", desc_data[1]["value"], second_text=desc_data[2]["value"]),
        _get_arrow_graph("使用身份"),
        _get_graph("icon-secret", desc_data[3]["value"]),
        _get_arrow_graph("发起主动认证请求", 150),
        _get_graph("icon-server", desc_data[0]["value"]),
    ]


def _408(desc_data, **kwargs):
    return [
        _get_graph("icon-computer", desc_data[0]["value"], second_text=desc_data[1]["value"]),
        _get_arrow_graph("使用身份"),
        _get_graph("icon-secret", desc_data[3]["value"]),
        _get_arrow_graph("触发特权登录"),
        _get_graph("icon-server", desc_data[2]["value"]),
    ]


def _409(desc_data, **kwargs):
    return [
        _get_graph("icon-computer", desc_data[0]["value"], second_text=desc_data[1]["value"]),
        _get_arrow_graph("使用身份"),
        _get_graph("icon-secret", desc_data[2]["value"]),
        _get_arrow_graph("通过约束委派获得目标身份", 200),
        _get_graph("icon-user", desc_data[3]["value"]),
        _get_arrow_graph("对该计算机的权限", 120),
        _get_graph("icon-computer", desc_data[4]["value"]),
    ]


def _410(desc_data, **kwargs):
    return [
        _get_graph("icon-computer", desc_data[0]["value"], second_text=desc_data[1]["value"]),
        _get_arrow_graph("使用身份"),
        _get_graph("icon-secret", desc_data[2]["value"]),
        _get_arrow_graph("使用MS14-068 EXP攻击域控", 250),
        _get_graph("icon-server", desc_data[3]["value"])
    ]


def _501(desc_data, **kwargs):
    return [
        _get_graph("icon-computer", desc_data[0]["value"], second_text=desc_data[1]["value"]),
        _get_arrow_graph("使用身份"),
        _get_graph("icon-secret", desc_data[2]["value"]),
        _get_arrow_graph("修改了", 250),
        _get_graph("icon-settings", ["AdminSDHolder"])
    ]


def _502(desc_data, **kwargs):
    return [
        _get_graph("icon-computer", desc_data[0]["value"], second_text=desc_data[1]["value"]),
        _get_arrow_graph("使用身份"),
        _get_graph("icon-secret", desc_data[2]["value"]),
        _get_arrow_graph("远程修改域内配置", 200),
        _get_graph("icon-server", desc_data[3]["value"])
    ]


def _503(desc_data, **kwargs):
    return [
        _get_graph("icon-computer", desc_data[0]["value"], second_text=desc_data[1]["value"]),
        _get_arrow_graph("使用身份"),
        _get_graph("icon-secret", desc_data[2]["value"]),
        _get_arrow_graph("重置了"),
        _get_graph("icon-settings", ["DSRM密码"])
    ]


def _504(desc_data, **kwargs):
    return [
        _get_graph("icon-computer", desc_data[0]["value"], second_text=desc_data[1]["value"]),
        _get_arrow_graph("使用身份"),
        _get_graph("icon-secret", desc_data[2]["value"]),
        _get_arrow_graph("添加委派权限"),
        _get_graph("icon-settings", ["组策略"])
    ]


def _505(desc_data, **kwargs):
    return [
        _get_graph("icon-computer", desc_data[0]["value"], second_text=desc_data[1]["value"]),
        _get_arrow_graph("使用身份"),
        _get_graph("icon-secret", desc_data[2]["value"]),
        _get_arrow_graph("向目标"),
        _get_graph("icon-user", desc_data[3]["value"]),
        _get_arrow_graph("添加高风险"),
        _get_graph("icon-privilege", ["约束委派权限"])
    ]


def _506(desc_data, **kwargs):
    return [
        _get_graph("icon-computer", desc_data[0]["value"], second_text=desc_data[1]["value"]),
        _get_arrow_graph("使用身份"),
        _get_graph("icon-secret", desc_data[2]["value"]),
        _get_arrow_graph("将目标用户"),
        _get_graph("icon-user", desc_data[3]["value"]),
        _get_arrow_graph("添加到"),
        _get_graph("icon-group", desc_data[4]["value"])
    ]


def _507(desc_data, **kwargs):
    return [
        _get_graph("icon-computer", desc_data[0]["value"], second_text=desc_data[1]["value"]),
        _get_arrow_graph("使用身份"),
        _get_graph("icon-secret", desc_data[2]["value"]),
        _get_arrow_graph("在域控上"),
        _get_graph("icon-server", desc_data[3]["value"]),
        _get_arrow_graph("创建系统服务"),
        _get_graph("icon-ServiceGroup", desc_data[4]["value"])
    ]


def _508(desc_data, **kwargs):
    return [
        _get_graph("icon-computer", desc_data[0]["value"], second_text=desc_data[1]["value"]),
        _get_arrow_graph("使用身份"),
        _get_graph("icon-secret", desc_data[2]["value"]),
        _get_arrow_graph("在域控上"),
        _get_graph("icon-server", desc_data[3]["value"]),
        _get_arrow_graph("创建计划任务"),
        _get_graph("icon-settings", desc_data[4]["value"])
    ]


def _509(desc_data, **kwargs):
    return [
        _get_graph("icon-computer", desc_data[0]["value"], second_text=desc_data[1]["value"]),
        _get_arrow_graph("使用身份"),
        _get_graph("icon-secret", desc_data[2]["value"]),
        _get_arrow_graph("修改目标"),
        _get_graph("icon-user", desc_data[3]["value"]),
        _get_arrow_graph("的属性"),
        _get_graph("icon-settings", ["SIDHistory"])
    ]


def _510(desc_data, **kwargs):
    return [
        _get_graph("icon-computer", desc_data[0]["value"], second_text=desc_data[1]["value"]),
        _get_arrow_graph("发起SkeletonKeys扫描", 200),
        _get_graph("icon-server", desc_data[2]["value"]),
        _get_arrow_graph("发现"),
        _get_graph("icon-settings", ["万能钥匙后门"])
    ]


def _511(desc_data, **kwargs):
    return [
        _get_graph("icon-computer", desc_data[0]["value"], second_text=desc_data[1]["value"]),
        _get_arrow_graph("伪造了目标"),
        _get_graph("icon-user", desc_data[2]["value"]),
        _get_arrow_graph("所属用户票据"),
        _get_graph("icon-ticket", ["TGT"])
    ]


def _512(desc_data, **kwargs):
    return [
        _get_graph("icon-computer", desc_data[0]["value"], second_text=desc_data[1]["value"]),
        _get_arrow_graph("认证目标"),
        _get_graph("icon-user", desc_data[2]["value"]),
        _get_arrow_graph("由域控处理"),
        _get_graph("icon-server", desc_data[3]["value"]),
        _get_arrow_graph("返回"),
        _get_graph("icon-settings", ["加密支持降级"]),
    ]


def _601(desc_data, **kwargs):
    return [
        _get_graph("icon-computer", desc_data[0]["value"], second_text=desc_data[1]["value"]),
        _get_arrow_graph("使用身份"),
        _get_graph("icon-secret", desc_data[2]["value"]),
        _get_arrow_graph("清空事件日志"),
        _get_graph("icon-server", desc_data[3]["value"])
    ]


def _602(desc_data, **kwargs):
    return [
        _get_graph("icon-server", desc_data[0]["value"]),
    ]


graph_map = {
    "101": _101,
    "102": _102,
    "103": _103,
    "104": _104,
    "201": _201,
    "202": _202,
    "203": _203,
    "301": _301,
    "302": _302,
    "303": _303,
    "304": _304,
    "305": _305,
    "306": _306,
    "401": _401,
    "402": _402,
    "403": _403,
    "404": _404,
    "405": _405,
    "406": _406,
    "407": _407,
    "408": _408,
    "409": _409,
    "410": _410,
    "501": _501,
    "502": _502,
    "503": _503,
    "504": _504,
    "505": _505,
    "506": _506,
    "507": _507,
    "508": _508,
    "509": _509,
    "510": _510,
    "511": _511,
    "512": _512,
    "601": _601,
    "602": _602,
}


def _get_graph(icon_name, text, second_text=None):
    if len(text) > 1:
        return _get_multi_graph(icon_name, text)
    else:
        return _get_single_graph(icon_name, text, second_text)


def _get_single_graph(icon_name, text, second_text=None):
    if not second_text:
        return {
            "type": "single",
            "icon": icon_name,
            "text": text[0]
        }
    else:
        return {
            "type": "single",
            "icon": icon_name,
            "text": text[0],
            "second_text": second_text[0]
        }


def _get_multi_graph(icon_name, text):
    return {
        "type": "multi",
        "icon": icon_name,
        "text": text
    }


def _get_arrow_graph(text, length=100):
    return {
        "type": "arrow",
        "text": text,
        "length": length
    }
