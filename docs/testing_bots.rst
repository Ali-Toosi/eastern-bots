Testing Your Bots
=================

You may test your bots however way you would prefer. But this is what I would recommend as it's simple to setup and
easy to run.

#.  | Create a test bot using `@BotFather <https://t.me/botfather>`_ for all your development work. It does not matter
        what you call it, it's not going to be deployed. I have called mine ``BotDevTestBot``.
#.  | In your bot folder, there is a file called ``bot.py``. There is a list of allowed bots in there ``allowed_bot_usernames``.
        Add your test bot's username in that list.
#.  | Install Ngrok from https://ngrok.com. Ngrok is an app that gives you a public address (https supported) for an app
        deployed on your local computer. We will use it to expose the project to the web so Telegram can send its updates
        to us.
#.  | Run the project using ``make up``. This will host the project on port 8000.
#.  | Run Ngrok on port 8000. It will give you two urls, copy the one that starts with *https://*.
#.  | Set your test bot's webhook to the URL given by Ngrok.
#.  | If all the steps are done successfully, your test bot should now run using the same source code as your bot.
        Test it by sending a message. If it's not working, look at your app logs for any errors.

.. note::

    Everytime you run Ngrok it will give you a new address and you will have to set the webhook again (last step above).
