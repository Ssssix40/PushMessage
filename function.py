import json
import requests

import config_default
from tools import merge

configs = config_default.configs

try:
    import config_override
    configs = merge(configs, config_override.configs)
except ImportError:
    pass


# 企业微信
# https://work.weixin.qq.com/api/doc/90000/90135/90236
def corWechatPusher(message):
    corID = configs['corWechat']['corID']
    corpsecret = configs['corWechat']['corpsecret']
    response = requests.get(
        'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=' + corID +
        '&corpsecret=' + corpsecret).text
    if "access_token" in response:
        access_token = json.loads(response)["access_token"]
        data = {
            "touser": configs['corWechat']['toUser'],
            "msgtype": "text",
            "agentid": configs['corWechat']['agentid'],
            "text": {
                "content": message
            },
            "safe": 0,
            "enable_id_trans": 0,
            "enable_duplicate_check": 0,
            "duplicate_check_interval": 1800
        }
        requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' +
            access_token,
            json=data)
    else:
        print(response)


# ios_bark
def bark(message):
    address = configs['bark']['ip']
    token = configs['bark']['token']
    requests.get(address + token + '/' + message)
