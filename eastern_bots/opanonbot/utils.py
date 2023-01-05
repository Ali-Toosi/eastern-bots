import string

from aiogram import Bot
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardRemove,
)
from asgiref.sync import sync_to_async
from django.utils.crypto import get_random_string

from eastern_bots.opanonbot import messages
from eastern_bots.opanonbot.models import Blocked, ChatCode


async def create_new_chat_code(tg_user_id):
    """
    Create a new unique code for this Telegram id and save it on ChatCode.
    :param tg_user_id: The Telegram id for which we want to create a new chat code.
    :return: The new chat code (not the object, the code itself).
    """
    chat_code, _ = await ChatCode.objects.aget_or_create(tg_user_id=tg_user_id)
    code = None
    while not code:
        code = get_random_string(
            7, allowed_chars=string.ascii_lowercase + string.digits
        )
        if await ChatCode.objects.filter(code=code).aexists():
            code = None
    chat_code.code = code
    await sync_to_async(chat_code.save)()
    return code


async def user_is_not_blocked(
    bot: Bot, m: messages.en.Messages, blocker_id, blocked_id
):
    if await Blocked.objects.filter(blocker=blocker_id, blocked=blocked_id).aexists():
        await bot.send_message(
            blocked_id, m.send_blocked, reply_markup=ReplyKeyboardRemove()
        )
        return False
    return True


async def chat_code_is_valid(bot: Bot, m: messages.en.Messages, code, tg_id):
    """
    Make sure the chat code exists and the user is not blocked.
    Return True if valid, False otherwise.
    """
    code = str(code)
    if not code:
        return False

    chat_code_qs = ChatCode.objects.filter(code=code)
    if not code or not await chat_code_qs.aexists():
        await bot.send_message(
            tg_id, m.send_link_not_found, reply_markup=ReplyKeyboardRemove()
        )
        return False

    destination = await chat_code_qs.afirst()
    dst_tg_id = destination.tg_user_id
    if not await user_is_not_blocked(bot, m, dst_tg_id, tg_id):
        return False

    return True


def anon_message_reply_markup(sender_tg_id, message_id):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="⬅️ Reply", callback_data=f"reply_{sender_tg_id}_{message_id}"
                ),
                InlineKeyboardButton(
                    text="❌ Block", callback_data=f"block_{sender_tg_id}"
                ),
            ]
        ]
    )
