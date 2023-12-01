import os
import sys


def printAuthStr(auth_str):
    print('\n\nBelow is your telegrest auth string ⬇️\n\n')
    print(auth_str)
    print('\nAbove is your telegrest auth string ⬆️\n\n')
    print('''
    - Keep this string safe! Dont leak it.
    - Anyone with this string can use it to login into your account and do anything they want to to do.
    - For more information about Telethon Session Strings
    \thttps://docs.telethon.dev/en/latest/concepts/sessions.html#string-sessions
    - You can deactivate this session by going to your
    \tTelegram App -> Settings -> Devices -> Active sessions
    ''')


def getInputFromKeyboard(of_what: str):
    val = os.getenv(of_what)
    if not val:
        val = input(f'Please enter your {of_what}:\n>')
        if not val:
            print('Recieved no input. Quitting.')
            sys.exit()
        return val
    return val
