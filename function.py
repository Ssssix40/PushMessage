import json
import time
import requests
import yagmail
from configparser import ConfigParser

configs = ConfigParser()
configs.read('config.ini')
configs.read('config_custom.ini')


# 企业微信
# https://work.weixin.qq.com/api/doc/90000/90135/90236
def corWechatPusher(method, message):
    data = {
        "touser": configs['corWechat']['toUser'],
        "msgtype": method,
        "agentid": configs['corWechat']['agentid'],
        method: {
            "content": message
        },
        "safe": 0,
        "enable_id_trans": 0,
        "enable_duplicate_check": 0,
        "duplicate_check_interval": 1800
    }
    corID = configs['corWechat']['corID']
    corpsecret = configs['corWechat']['corpsecret']
    access_token = configs['corWechat']['access_token']
    overtime = configs['corWechat']['overtime']
    if time.time() > float(overtime):
        print('timeover')
        response = requests.get(
            'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=' + corID +
            '&corpsecret=' + corpsecret).text
        configs['corWechat']['overtime'] = str(time.time() + 7000)
        access_token = json.loads(response)["access_token"]
        configs['corWechat']['access_token'] = access_token

    return requests.post(
        'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' +
        access_token,
        json=data).text


# ios_bark
def bark(message):
    url = configs['bark']['ip']
    token = configs['bark']['token']
    return requests.get(url + token + '/' + message).text


def flomo(message):
    url = configs['flomo']['url']
    payload = {'content': message}
    return requests.post(url, json=payload).text


def mail(towho, title, content):
    url = configs['mail']['url']
    user = configs['mail']['user']
    password = configs['mail']['password']
    print(url, user, password, title, content, towho)
    yag = yagmail.SMTP(user=user, password=password, host=url)
    yag.send(towho, title, content)
    return '''
    to: %s,
    title: %s,
    content: %s
    ''' % (towho, title, content)
