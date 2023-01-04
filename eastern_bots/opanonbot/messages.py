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

    That means no one will be able to send you any more messages unless they have your new code.
    They won't be able to reply to your old messages either.

    Are you sure you want to get a new code?
"""
)
new_code_created = "Here is your new chat code: `{code}` (click to copy)"
