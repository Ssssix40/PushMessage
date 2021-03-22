from fastapi import FastAPI
import function

app = FastAPI()


@app.get("/corwechat/{message}")
async def corwechat(message: str):
    return function.corWechatPusher(message)


@app.get("/bark/{message}")
async def bark(message: str):
    return function.bark(message)


@app.get('/flomo/{message}')
async def flomo(message: str):
    return function.flomo(message)
