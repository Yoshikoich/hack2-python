"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(s):
    _str = {k.capitalize(): v.capitalize()[:-3] + v[-2:] for k, v in d.items() if v.startswith(k)}
    result = _str
    return result
