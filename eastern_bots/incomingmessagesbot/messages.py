from textwrap import dedent

start_message = dedent(
    """\
    *Use me to create webhooks for sending messages to chats!*

    /help - to learn what a webhook is and how you can use them.
    /new - to create a new webhook (send this in the chat you want to create the webhook for).
    /list - to list the webhooks of this chat
"""
)

help_message = dedent(
    """\
    *What is a webhook?*
    A webhook is basically a URL. When you create a webhook you will create a URL. The URL can then be used for having
    the bot send a message in a chat.

    *How do I use a webhook?*
    Let's say your webhook address is `www.domain.com/webhook`. If you `POST` this request to this address:
    ```
    {
        "message": "... some text ..."
    }
    ```
    Then you will see the bot sends a message saying "... some text ..." to the chat you originally created the webhook
    in.

    *Can I send pictures too?*
    Not yet :( As of now you can only send text messages from the webhook. But hey! We are open source. Come contribute
    and add the features you would like to have! https://github.com/Ali-Toosi/Eastern-Bots
"""
)

cancel_message = "It's all cancelled now! You may start over, or go to /start."
