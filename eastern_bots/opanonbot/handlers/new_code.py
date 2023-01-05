from aiogram import Bot, F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove

from ...utils.common_keyboards import confirmation_keyboard
from .. import messages
from ..bot import dp
from ..models import ChatCode
from ..utils import create_new_chat_code


class RevokeStates(StatesGroup):
    requested = State()


@dp.message(Command(commands=["new_code"]))
async def new_code_request(
    message: types.Message, state: FSMContext, m: messages.en.Messages
):
    await state.clear()
    tg_id = message.chat.id
    has_code = await ChatCode.objects.filter(tg_user_id=tg_id).aexists()
    if not has_code:
        code = await create_new_chat_code(tg_id)
        await message.reply(
            m.new_code_created.format(code=code), reply_markup=ReplyKeyboardRemove()
        )
    else:
        await state.set_state(RevokeStates.requested)
        await message.reply(
            m.new_code_confirmation,
            reply_markup=confirmation_keyboard(yes=m.yes_do_it, no=m.no_cancel),
        )


@dp.message(RevokeStates.requested, F.text.in_(messages.union.yes_do_it))
async def new_code_confirmed(
    message: types.Message, bot: Bot, state: FSMContext, m: messages.en.Messages
):
    tg_id = message.chat.id
    code = await create_new_chat_code(tg_id)
    await state.clear()
    await message.reply(
        m.new_code_created.format(code=code),
        reply_markup=ReplyKeyboardRemove(),
        parse_mode="markdown",
    )
    bot_username = (await bot.get_me()).username
    await bot.send_message(tg_id, f"https://t.me/{bot_username}?start=C{code}")


@dp.message(RevokeStates.requested, F.text.in_(messages.union.no_cancel))
async def new_code_not_confirmed(
    message: types.Message, state: FSMContext, m: messages.en.Messages
):
    await state.clear()
    await message.reply(
        m.delete_code_cancelled,
        reply_markup=ReplyKeyboardRemove(),
    )


@dp.message(RevokeStates.requested)
async def unknown(message: types.Message, m: messages.en.Messages):
    await message.reply(m.confirmation_keyboard_ignored)
