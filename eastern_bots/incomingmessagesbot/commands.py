"""
List of BotCommand objects. Can be used in code but the main purpose is for utils.setup_bot command to read them
and set them on the bot API.
"""
from aiogram.types import BotCommand

commands = [
    BotCommand(command="start", description="Start the bot"),
    BotCommand(command="new", description="Create a new webhook for this chat"),
    BotCommand(command="list", description="List webhooks created for this chat"),
    BotCommand(command="help", description="How to use this bot"),
    BotCommand(command="cancel", description="Cancel whatever is happening"),
]

bot_map = {
    "incomingmessagesbot": commands,
    "botdevtestbot": commands,
}
