from fastapi import FastAPI
import function


app = FastAPI()


@app.get("/corwechat/{message}")
async def corwechat(message: str):
    function.corWechatPusher(message)
    return 'done'


@app.get("/bark/{message}")
async def corwechat(message: str):
    function.bark(message)
    return 'done'