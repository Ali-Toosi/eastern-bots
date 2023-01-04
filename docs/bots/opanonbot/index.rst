.. _incomingmessagesbot_index:

Incoming Messages Bot
=====================

https://t.me/IncomingMessagesBot

This bot allows you to send messages in chats by calling a **webhook**.

1. Add the bot to the chat you would like to have a webhook for (you can also use the private chat with bot for this).
2. Call ``/new`` command on the bot and follow the prompts.
3. The bot will send a URL which is that chat's webhook.
4. Post messages to that webhook with ``message`` key and the message will be sent to the chat, by the bot.

.. note::
    The bot only supports **text** messages at the moment. You may not post pictures or other message types to the webhook

Commands
--------
``/new``
    This will create a new webhook for the chat the command was sent to. The webhook address will be sent in the chat.
``/help``
    Help message explaining what the bots and its commands are.
``/list``
    Show all the webhooks created in this chat. From the sent list, you can get the URL for a webhook again or delete it.

Contributing
------------

Check out this page for a list of things you can work on: :ref:`Contributing Guide <incomingmessagesbot_contributing>`
