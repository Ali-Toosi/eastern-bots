from aiogram import F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove

from ...utils.common_keyboards import confirmation_keyboard
from .. import messages as m
from ..bot import dp
from ..models import ChatCode


class DeletionStates(StatesGroup):
    requested = State()


@dp.message(Command(commands=["delete_code"]))
async def delete_code_request(message: types.Message, state: FSMContext):
    await state.clear()
    tg_id = message.chat.id
    has_code = await ChatCode.objects.filter(tg_user_id=tg_id).aexists()
    if not has_code:
        await message.reply(m.delete_code_no_code, reply_markup=ReplyKeyboardRemove())
    else:
        await state.set_state(DeletionStates.requested)
        await message.reply(
            m.delete_code_confirmation,
            reply_markup=confirmation_keyboard(yes="Yes, delete."),
        )


@dp.message(DeletionStates.requested, F.text == "Yes, delete.")
async def delete_code_confirmed(message: types.Message, state: FSMContext):
    tg_id = message.chat.id
    await ChatCode.objects.filter(tg_user_id=tg_id).adelete()
    await state.clear()
    await message.reply(m.delete_code_deleted, reply_markup=ReplyKeyboardRemove())


@dp.message(DeletionStates.requested, F.text == "No, cancel.")
async def delete_code_not_confirmed(message: types.Message, state: FSMContext):
    await state.clear()
    await message.reply(
        "Cancelled! You may keep chatting.", reply_markup=ReplyKeyboardRemove()
    )


@dp.message(DeletionStates.requested)
async def unknown(message: types.Message):
    await message.reply("I didn't get that. Use the keyboard:")
