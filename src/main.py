import uvicorn
from asgiref.wsgi import WsgiToAsgi
from flask import Flask, request, jsonify
from telethon import TelegramClient
import sys

from telethon.sessions import StringSession

from authorizer import telegrest_authorize
from src.service import do_send_message, do_send_file
from util import getEnvParam, getApiId, getApiHash, getSessionString

auth_str = getEnvParam('TELEGREST_AUTH', None)

if auth_str is None:
    telegrest_authorize()
    sys.exit()

api_id = getApiId(auth_str)
api_hash = getApiHash(auth_str)
session_string = getSessionString(auth_str)

client = TelegramClient(StringSession(session_string), api_id, api_hash)

app = Flask(__name__)
asgi_app = WsgiToAsgi(app)


@app.route('/send_message', methods=['POST'])
async def send_message():
    return await do_send_message(client)


@app.route('/send_file', methods=['POST'])
async def send_file():
    return await do_send_file(client)


async def start():
    await client.start()
    config = uvicorn.Config("__main__:asgi_app", host='0.0.0.0', port=5001, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    client.loop.run_until_complete(start())
