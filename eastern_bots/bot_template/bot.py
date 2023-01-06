import typing as t

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from asgiref.sync import sync_to_async

from eastern_bots.utils.bot_state_storage import DjangoCacheStorage

dp = Dispatcher(storage=DjangoCacheStorage())


@dp.message.outer_middleware()
async def save_user_and_chat_middleware(
    handler, event: Message, data: t.Dict[str, t.Any]
):

    # Import the actual models from your app not the template versions
    from eastern_bots.bot_template.models import TelegramChat, TelegramUser

    chat: TelegramChat
    chat, _ = await TelegramChat.objects.aget_or_create(
        telegram_id=event.chat.id, type=event.chat.type
    )

    if chat.username != event.chat.username or chat.title != event.chat.title:
        chat.username = event.chat.username
        chat.title = event.chat.title
        await sync_to_async(chat.save)()

    user: t.Optional[TelegramUser] = None
    if (
        chat.type != TelegramChat.ChatTypes.CHANNEL
        and not event.sender_chat
        and event.from_user
    ):
        from_user = event.from_user
        field_names = ["first_name", "last_name", "username", "is_bot"]
        try:
            user = await TelegramUser.objects.aget(telegram_id=from_user.id)
            dirty = False
            for field_name in field_names:
                if getattr(user, field_name) != getattr(from_user, field_name):
                    setattr(user, field_name, getattr(from_user, field_name))
                    dirty = True
            if dirty:
                await sync_to_async(user.save)()
        except TelegramUser.DoesNotExist:
            user = await TelegramUser.objects.acreate(
                telegram_id=from_user.id,
                **{
                    field_name: getattr(from_user, field_name)
                    for field_name in field_names
                }
            )

    data["chat"] = chat
    data["user"] = user

    return await handler(event, data)


bot_instances = {}
allowed_bot_usernames = [x.lower() for x in ["BotDevTestBot"]]


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
    from .handlers import help  # noqa: F401 isort:skip


load_handlers()
