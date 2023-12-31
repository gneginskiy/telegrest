Telegrest: REST API Gateway for Telegram notifications
========
.. epigraph::

  ⭐️ Thanks **everyone** who has starred the project, it means a lot!

**Telegrest** is a straightforward application that lets you send Telegram notifications via REST API endpoints. It uses the Telethon library and comes packaged as a Docker image for easy deployment. Notably, it avoids the Telegram Bot API, opting for a regular client instead.

What is this?
-------------
Telegram stands out as a widely-used messaging application. 
This tool simplifies the process of creating programs that can send Telegram notifications through REST.


Installing
----------
0. Install docker ( https://docs.docker.com/engine/install/ )
1. Run the application from terminal/command line in interactive mode: 

.. code-block:: sh
  
  docker run -it gneginskiy/telegrest:1.0

2. Enter your api_id (e.g. 23491234). You can get it from https://my.telegram.org/apps
3. Enter your api_hash (e.g. 810a8615724f34f40676c2cab8d5b609). You can get it from https://my.telegram.org/apps
4. Enter you phone using international format (e.g. +79660354444)
5. Then, telegram will send you a confirmation code. Enter your confirmation code as well.
6. As an additional measure, telegram client can ask you for a password. Enter it as well.
7. After you provided all the required information, the application will print your **TELEGREST_AUTH** string. Save it, you'll need it soon.
8. Run the application from terminal/command line, providing the **TELEGREST_AUTH** string you got during the previous step:

.. code-block:: sh

  docker run \
  -p 5001:5001 \
  -e TELEGREST_AUTH=%YOUR_TELEGREST_AUTH_STRING_HERE% \
  gneginskiy/telegrest:1.0

9. Do not share your auth string with anybody.

Endpoints
-----------
For now, there are 2 endpoints, one for sending text messages, and another for sending files. 

1. Sending messages

**POST** ``http://localhost:5001/send_message``

.. code-block:: json

  {
      "username":"+79660354444",
      "message":"Hey!"
  }

For "username" field you can use the phone number as well as the actual telegram nickname (e.g. @addaxbx):

.. code-block:: json

  {
      "username":"addaxbx",
      "message":"Hey!"
  }


2. sending files: 

**POST** ``http://localhost:5001/send_file``

for ``data`` field base64 is used.

.. code-block:: json

  {
  "username":"addaxbx",
  "extension":"png",
  "data":"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"
  }

Additional features
-----------
To send text and files to "saved messages", just specify ``me`` as a username:


**POST** ``http://localhost:5001/send_message``

.. code-block:: json

  {
      "username":"me",
      "message":"reminder message for myself"
  }


Important note 
-----------
1. The TELEGREST_AUTH key should not be used under two different IP addresses simultaneously, otherwise it can no longer be used and will be revoked. Use the same session exclusively, or use different sessions, generating a separate TELEGREST_AUTH key for each application. 
2. Due to anti-spam telegram policies, some accounts (reported ones, or new ones) cannot initiate a discussion sending a message to the person outside of contact list. Thus, Telegrest gateway will only be able to do as much as linked telegram account allowed to.
3. Since the authentication feature is not there(at least for now), if you deploy Telegrest as a side container for some other app on the same host, feel free to restrict outside traffic to the application port(5001):

.. code-block:: sh

  sudo iptables -A INPUT -p tcp --dport 5001 -i lo -j ACCEPT
  sudo iptables -A INPUT -p tcp --dport 5001 -j DROP

you can also run the app like this, it will restrict outside traffic as well:

.. code-block:: sh

  docker run \
  -p 127.0.0.1:5001:5001 \
  -e TELEGREST_AUTH=%YOUR_TELEGREST_AUTH_STRING_HERE% \
  gneginskiy/telegrest:1.0

4. As with any third-party library for Telegram, be careful not to break `Telegram's Terms of Service`_ or `Telegram can ban the account`_.



.. _Telegram: https://telegram.org
.. _Telegram's Terms of Service: https://core.telegram.org/api/terms
.. _Telegram can ban the account: https://docs.telethon.dev/en/stable/quick-references/faq.html#my-account-was-deleted-limited-when-using-the-library
