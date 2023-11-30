from telethon import TelegramClient

from telethon.sessions import StringSession

from src.console import getInputFromKeyboard, printAuthStr
from src.util import AUTH_DELIMITER, to_base64


def telegrest_authorize():
    api_id = int(getInputFromKeyboard('api_id'))
    api_hash = getInputFromKeyboard('api_hash')
    tmp_client = TelegramClient(None, api_id, api_hash).start()
    auth_str = str(api_id) + AUTH_DELIMITER + api_hash + AUTH_DELIMITER + StringSession.save(tmp_client.session)
    auth_str = to_base64(auth_str)
    printAuthStr(auth_str)
