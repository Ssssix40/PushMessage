import requests


# 获取ip地址
def getIP():
    ip = requests.get('https://checkip.amazonaws.com').text.strip()
    return ip


# https://github.com/michaelliao/awesome-python3-webapp/blob/day-06/www/config.py
def merge(defaults, override):
    r = {}
    for k, v in defaults.items():
        if k in override:
            if isinstance(v, dict):
                r[k] = merge(v, override[k])
            else:
                r[k] = override[k]
        else:
            r[k] = v
    return r
