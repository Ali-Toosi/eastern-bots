from aiogram import Bot, Dispatcher

from eastern_bots.utils.bot_state_storage import DjangoCacheStorage

dp = Dispatcher(storage=DjangoCacheStorage())

bot_instances = {}
allowed_bot_usernames = [x.lower() for x in ["BotDevTestBot"]]


def get_bot_instance(token):
    if token not in bot_instances.keys():
        bot = Bot(token)
        if str(bot.get_me().username).lower() not in allowed_bot_usernames:
            return None
        bot_instances[token] = bot
    return bot_instances[token]
