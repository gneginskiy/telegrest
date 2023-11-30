from flask import Flask, request, jsonify
import os

from src.util import saveBase64ToBinaryFile


async def do_send_message(client):
    data = request.get_json()
    username = data['username']
    message = data['message']
    print("sending: "+ username + " " + message)
    print("remote addr: "+ request.remote_addr)
    await client.send_message(username, message)
    return jsonify({}), 200


async def do_send_file(client):
    jsonRq = request.get_json()
    username = jsonRq['username']
    base64Data = jsonRq['data']
    extension = jsonRq['extension']
    tmpFilePath = saveBase64ToBinaryFile(base64Data, extension)
    print("remote addr: " + request.remote_addr)
    print("sending " + extension + " file to: " + username)
    try:
        await client.send_file(username, tmpFilePath)
        return jsonify({}), 200
    finally:
        if os.path.exists(tmpFilePath):
            os.remove(tmpFilePath)
