from textwrap import dedent

language = "en"


class Messages:
    command_start = "See how everything works"
    command_help = "Tips and help for using the bot"
    command_my_link = "Get your chat link for receiving anonymous messages"
    command_new_link = "Delete your old chat link and create a new one"
    command_delete_link = "Delete your chat link and don't create a new one"
    command_cancel = "Cancel whatever is happening"

    start_message = dedent(
        """\
        *Receive anonymous messages*
        Click on /my\\_link and get your link. Others can send you a message if they have your link.

        You can delete your link with /delete\\_link or get a new one with /new\\_link.

        *Tips and Help*
        You may click on /help to get answers to some commonly asked questions.
    """
    )

    help_message = (
        "*How do I use this bot?*\n"
        "Click on /my\\_link and get your link. Whoever has this link can send you anonymous messages.\n"
        "Put your link on your social media and ask questions from your followers."
        "\n\n"
        "*Can you see the messages I send?*\n"
        "No, everything is anonymous... and open source. Confirm for yourself (and contribute!): "
        "[source code](https://github.com/Ali-Toosi/eastern-bots/tree/main/eastern_bots/opanonbot)"
        "\n\n"
        "*How do I unblock someone?*\n"
        "You can't. Once they are blocked, they are blocked forever."
        "\n\n"
        "*Can I add more features to the bot?*"
        "Yes! This is an open source project and contributions are very welcome.\n"
        "https://github.com/Ali-Toosi/eastern-bots"
    )

    all_cancelled = "All cancelled! What's next? /start?"

    show_link = dedent(
        """\
        Anyone with this link can send you a message (unless they are blocked).

        You can delete your link with /delete\\_link or get a new one with /new\\_link.

        👇 Your link 👇
    """
    )

    delete_link_no_link = (
        "You don't have any chat links to delete. Click on /my_link to create one."
    )
    delete_link_confirmation = (
        "Are you sure you want to delete your chat link? No one would be able to send you messages"
        " with this link anymore."
    )
    delete_link_deleted = (
        "Your chat link has been deleted. You can get a new one with /my_link."
    )
    delete_link_cancelled = "Cancelled! You may keep using your old link."

    new_link_confirmation = dedent(
        """\
        Creating a new link deletes your old link.

        Are you sure you want to get a new link?
    """
    )
    new_link_created = "Here's your new chat link:"

    send_link_not_found = "This link doesn't exist."
    send_blocked = "Seems like this person has blocked you from sending more messages 😞"
    send_ask_message = "Send your anonymous message... (or /cancel)"
    send_successful = "Message sent! I'll let you know if they reply."
    send_failed = (
        "Failed to send the message! Maybe they have stopped the bot. Try with a different message. If this "
        "keeps happening, they are probably not using the bot anymore and don't receive messages."
    )

    no_self_messaging = (
        "You can't send yourself a message. That wouldn't be very anonymous."
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
