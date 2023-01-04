"""
List of BotCommand objects. Can be used in code but the main purpose is for utils.setup_bot command to read them
and set them on the bot API.
"""
from aiogram.types import BotCommand

commands = [
    BotCommand(command="start", description="See how everything works"),
    BotCommand(command="help", description="Tips and help for using the bot"),
    BotCommand(
        command="send",
        description="Send anonymous messages to someone with their chat code",
    ),
    BotCommand(
        command="receive",
        description="Get your chat code for receiving anonymous messages",
    ),
    BotCommand(
        command="new_code", description="Delete your old chat code and create a new one"
    ),
    BotCommand(
        command="delete_code",
        description="Delete your chat code and don't create a new one",
    ),
]
