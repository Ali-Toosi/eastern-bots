"""
List of BotCommand objects. Can be used in code but the main purpose is for utils.setup_bot command to read them
and set them on the bot API.
"""
from aiogram.types import BotCommand

from .messages import en, fa

base_commands = [
    ("start", "command_start"),
    ("help", "command_help"),
    ("my_link", "command_my_link"),
    ("new_link", "command_new_link"),
    ("delete_link", "command_delete_link"),
    ("cancel", "command_cancel"),
]

per_lang = {"en": [], "fa": []}

for lang in [en, fa]:
    for command in base_commands:
        per_lang[lang.language].append(
            BotCommand(
                command=command[0], description=getattr(lang.Messages, command[1])
            )
        )

bot_map = {
    "opanonbot": per_lang["en"],
    "nashenasbot": per_lang["fa"],
    "botdevtestbot": per_lang["en"],
}
