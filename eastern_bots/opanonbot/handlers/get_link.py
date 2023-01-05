from aiogram import Bot, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

from .. import messages
from ..bot import dp
from ..models import ChatCode
from ..utils import create_new_chat_code


@dp.message(Command(commands=["my_link"]))
async def get_link(
    message: types.Message, state: FSMContext, bot: Bot, m: messages.en.Messages
):
    await state.clear()
    tg_id = message.chat.id
    try:
        code = (await ChatCode.objects.aget(tg_user_id=tg_id)).code
    except ChatCode.DoesNotExist:
        code = await create_new_chat_code(tg_id)
    await message.reply(
        m.show_link.format(code=code),
        reply_markup=ReplyKeyboardRemove(),
        parse_mode="markdown",
    )
    bot_username = (await bot.get_me()).username
    await bot.send_message(
        tg_id,
        f"https://t.me/{bot_username}?start=C{code}",
        disable_web_page_preview=True,
    )
