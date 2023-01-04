from aiogram import types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

from .. import messages as m
from ..bot import dp
from ..models import ChatCode
from ..utils import create_new_chat_code


@dp.message(Command(commands=["receive"]))
async def get_code(message: types.Message, state: FSMContext):
    await state.clear()
    tg_id = message.chat.id
    try:
        code = (await ChatCode.objects.aget(tg_user_id=tg_id)).code
    except ChatCode.DoesNotExist:
        code = await create_new_chat_code(tg_id)
    await message.reply(
        m.show_code.format(code=code),
        reply_markup=ReplyKeyboardRemove(),
        parse_mode="markdown",
    )
