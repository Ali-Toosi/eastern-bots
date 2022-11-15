from aiogram import Bot, Dispatcher

from eastern_bots.utils.bot_state_storage import DjangoCacheStorage

dp = Dispatcher(storage=DjangoCacheStorage())

bot_instances = {}
allowed_bot_usernames = [x.lower() for x in ["BotDevTestBot", "IncomingMessagesBot"]]


async def get_bot_instance(token):
    if token not in bot_instances.keys():
        bot = Bot(token)
        bot_profile = await bot.get_me()
        if str(bot_profile.username).lower() not in allowed_bot_usernames:
            return None
        bot_instances[token] = bot
    return bot_instances[token]
