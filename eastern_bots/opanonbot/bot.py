import typing as t

from aiogram import Bot, Dispatcher, types

from eastern_bots.opanonbot import messages
from eastern_bots.utils.bot_state_storage import DjangoCacheStorage

dp = Dispatcher(storage=DjangoCacheStorage())


@dp.callback_query.outer_middleware()
@dp.message.outer_middleware()
async def save_user_and_chat_middleware(
    handler, event: types.Message, data: t.Dict[str, t.Any]
):
    bot_username = (await data["bot"].get_me()).username.lower()
    data["m"] = messages.bot_map[bot_username]

    return await handler(event, data)


bot_instances = {}
allowed_bot_usernames = [
    x.lower() for x in ["BotDevTestBot", "OpanonBot", "NashenasBot"]
]


async def get_bot_instance(token) -> t.Optional[Bot]:
    if token not in bot_instances.keys():
        bot = Bot(token)
        bot_profile = await bot.get_me()
        if str(bot_profile.username).lower() not in allowed_bot_usernames:
            return None
        bot_instances[token] = bot
    return bot_instances[token]


def load_handlers():
    """
    Loads the handlers so they would be registered with the dispatcher.
    The order of registration determines the order they are run, hence ignoring isort and ordering them manually.
    """
    from .handlers import (  # noqa: F401 isort:skip
        start,
        delete_link,
        get_link,
        new_link,
        block,
        chat,
        unknown,
    )


load_handlers()
