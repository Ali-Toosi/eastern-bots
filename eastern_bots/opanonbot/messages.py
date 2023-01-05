from textwrap import dedent

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
    "[source code](https://github.com/Ali-Toosi/eastern-bots/tree/main/eastern_bots/opanonbot) "
)

show_code = dedent(
    """\
    This is your chat code: `{code}` (click to copy).

    Anyone with this code can send you a message (unless they are blocked).

    You can delete your code with /delete\\_code or get a new one with /new\\_code.
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

new_code_confirmation = dedent(
    """\
    Creating a new code deletes your old code.

    You won't receive any new messages or any replies to your old messages. You can still start a new chat with someone
    if you have their code.

    Are you sure you want to get a new code?
"""
)
new_code_created = "Here is your new chat code: `{code}` (click to copy)"

send_ask_code = (
    "Send the code of the person you want to chat to (they should provide the code):"
)
send_code_not_found = "This code doesn't exist. Try again? 👉 /send"
send_you_need_code = (
    "You need to have a code before sending messages so you can receive replies. Click on /receive "
    "to get your code."
)
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
