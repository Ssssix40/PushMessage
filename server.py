from fastapi import FastAPI
import function

app = FastAPI()


@app.get("/corwechat/{method}")
async def corwechat(message: str, method: str):
    if method == 'markdown':
        message = message.replace(r'\n', '\n')
        message = message.replace('@', '#')
    else:
        method = 'text'
    return function.corWechatPusher(method, message)


@app.get("/bark/{message}")
async def bark(message: str):
    return function.bark(message)


@app.get('/flomo/{message}')
async def flomo(message: str):
    return function.flomo(message)
