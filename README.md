# PushMessege

## Features

1. 企业微信应用推送文字消息
2. ios bark应用推送文字消息

## Usage

1. `pip install -r requirements.txt`
1. 修改`config`文件
1. `uvicorn server:app`
1. `server/corwechat/message`或者`server/bark/message`调用

## TODO

1. 完善已有的各种推送方式(比如企业微信可以推送图片)
2. 完善api功能
