# PushMessege

## Features

1. 企业微信应用推送文字消息
2. ios bark应用推送文字消息
3. 推送文字到flomo

## Usage

1. `pip install -r requirements.txt`
1. 修改`config.ini`文件或者创建`config_custom.ini`文件, 并对应`config.ini`文件自定义对应的键
1. `uvicorn server:app`
1. `server/function/message`调用

## TODO

1. 完善已有的各种推送方式(比如企业微信可以推送图片)
2. 增加各类api功能(其实目前我会用到的就企业微信,bark还有flomo,后续发现继续补充)

## 更新日志

### 0.1.2

1. 增加flomo推送方式
1. 使用个人觉得更优雅的config方式(configparser)
1. 给企业微信方式增加了一个token过期验证, 少一个get或许能快点吧
