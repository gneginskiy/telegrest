Telegrest
========
.. epigraph::

  ⭐️ Thanks **everyone** who has starred the project, it means a lot!

**Telegrest** is a simple REST application which allows you to seamlessly send telegram notifications (text messages as well as files) via REST API endpoints.
The application is built upon telethon, and packaged as a docker image, so you would be able to run it anywhere with little to no pain. 

What is this?
-------------
Telegram is a popular messaging application. This app is meant
to make it easy for you to write programs that can send Telegram 
notification via REST.


Installing
----------
0. Install docker ( https://docs.docker.com/engine/install/ )
1. Run the application from terminal/command line in interactive mode: 
.. code-block:: sh

  docker run -it gneginskiy/telegrest:1.0

2. Enter your api_id (e.g. 23491234). You can get it from https://my.telegram.org/apps
3. Enter your api_hash (e.g. 810a8615724f34f40676c2cab8d5a609). You can get it from https://my.telegram.org/apps
4. Enter you phone using international format (e.g. +79660354444)
5. Then, telegram will send you a confirmation code. Enter your confirmation code as well.
6. As an additional measure, telegram client can ask you for a password. Enter it as well.
7. After you provided all the required information, the application will print *auth string*. Save it, you'll need it soon.
8. Run the application from terminal/command line, providing the *auth string* you got during the previous step:

.. code-block:: sh

  docker run \
  -p 5001:5001 \
  -e TELEGREST_AUTH=%YOUR_AUTH_STRING_HERE% \
  gneginskiy/telegrest:1.0

Creating a client
-----------------

.. code-block:: python

    from telethon import TelegramClient, events, sync

    # These example values won't work. You must get your own api_id and
    # api_hash from https://my.telegram.org, under API Development.
    api_id = 12345
    api_hash = '0123456789abcdef0123456789abcdef'

    client = TelegramClient('session_name', api_id, api_hash)
    client.start()


Doing stuff
-----------

.. code-block:: python

    print(client.get_me().stringify())

    client.send_message('username', 'Hello! Talking to you from Telethon')
    client.send_file('username', '/home/myself/Pictures/holidays.jpg')

    client.download_profile_photo('me')
    messages = client.get_messages('username')
    messages[0].download_media()

    @client.on(events.NewMessage(pattern='(?i)hi|hello'))
    async def handler(event):
        await event.respond('Hey!')


Next steps
----------

Do you like how Telethon looks? Check out `Read The Docs`_ for a more
in-depth explanation, with examples, troubleshooting issues, and more
useful information.

.. _asyncio: https://docs.python.org/3/library/asyncio.html
.. _MTProto: https://core.telegram.org/mtproto
.. _Telegram: https://telegram.org
.. _Compatibility and Convenience: https://docs.telethon.dev/en/stable/misc/compatibility-and-convenience.html
.. _Telegram's ToS: https://core.telegram.org/api/terms
.. _Telegram can ban the account: https://docs.telethon.dev/en/stable/quick-references/faq.html#my-account-was-deleted-limited-when-using-the-library
.. _Read The Docs: https://docs.telethon.dev

.. |logo| image:: logo.svg
    :width: 24pt
    :height: 24pt
