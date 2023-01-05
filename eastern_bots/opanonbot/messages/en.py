from textwrap import dedent

language = "en"


class Messages:
    command_start = "See how everything works"
    command_help = "Tips and help for using the bot"
    command_send = "Send anonymous messages to someone using their chat code"
    command_receive = "Get your chat code for receiving anonymous messages"
    command_new_code = "Delete your old chat code and create a new one"
    command_delete_code = "Delete your chat code and don't create a new one"

    start_message = dedent(
        """\
        *Send anonymous messages*
        Click on /send, give the code, start messaging!

        *Receive anonymous messages*
        Click on /receive and get your code. Others can send you a message if they have your code.

        You can delete your code with /delete\\_code or get a new one with /new\\_code.

        *Tips and Help*
        You may click on /help to get answers to some commonly asked questions.
    """
    )

    help_message = (
        "*Can you see the messages I send?*\n"
        "No, everything is anonymous... and open source. Confirm for yourself (and contribute!): "
        "[source code](https://github.com/Ali-Toosi/eastern-bots/tree/main/eastern_bots/opanonbot)"
        "\n\n"
        "*How do I unblock someone?*\n"
        "You can't. Once they are blocked, they are blocked forever."
        "\n\n"
        "*What's the difference between my code and my link?*\n"
        "Nothing really. If someone has your link, they can click on it and jump in the chat. If they only have your"
        " code, then they must press /send, give your code, then start chatting."
        "\n\n"
        "*Can I add more features to the bot?*"
        "Yes! This is an open source project and contributions are very welcome.\n"
        "https://github.com/Ali-Toosi/eastern-bots"
    )

    show_code = dedent(
        """\
        This is your chat code: `{code}` (click to copy).

        Anyone with this code can send you a message (unless they are blocked).

        You can delete your code with /delete\\_code or get a new one with /new\\_code.

        Or you can share a link instead of the code:
    """
    )

    delete_code_no_code = (
        "You don't have any chat codes to delete. Click on /receive to create one."
    )
    delete_code_confirmation = (
        "Are you sure you want to delete your chat code? No one would be able to send you messages"
        " with this code anymore."
    )
    delete_code_deleted = (
        "Your chat code has been deleted. You can get a new one with /receive."
    )
    delete_code_cancelled = "Cancelled! You may keep using your old code."

    new_code_confirmation = dedent(
        """\
        Creating a new code deletes your old code.

        Are you sure you want to get a new code?
    """
    )
    new_code_created = (
        "Here is your new chat code: `{code}` (click to copy)\n" "And your new link:"
    )

    send_ask_code = "Send the code of the person you want to chat to (they should provide the code):"
    send_code_not_found = "This code doesn't exist. Try again? 👉 /send"
    send_blocked = "Seems like this person has blocked you from sending more messages 😞"
    send_ask_message = "Send your anonymous message..."
    send_successful = "Message sent! I'll let you know if they reply."
    send_failed = (
        "Failed to send the message! Maybe they have stopped the bot. Try with a different message. If this "
        "keeps happening, they are probably not using the bot anymore and don't receive messages."
    )

    new_anonymous_chat = "New anonymous chat!"

    block_confirmation = "Are you sure you want to block this user? You will never receive messages from them again."
    user_blocked = "User blocked! You won't hear from them again."
    block_cancelled = "Cool. No one gets blocked : )"

    unknown_message = "Don't know what that is 🤷‍♀️\nMaybe press /start?"
    confirmation_keyboard_ignored = "I didn't get that. Use the keyboard:"

    yes_delete = "Yes, delete."
    no_cancel = "No, cancel."
    yes_do_it = "Yes, do it!"
    yes_block = "Yes, block!"
