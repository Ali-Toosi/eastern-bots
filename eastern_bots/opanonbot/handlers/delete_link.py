from aiogram import F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove

from ...utils.common_keyboards import confirmation_keyboard
from .. import messages
from ..bot import dp
from ..models import ChatCode


class DeletionStates(StatesGroup):
    requested = State()


@dp.message(Command(commands=["delete_link"]))
async def delete_code_request(
    message: types.Message, state: FSMContext, m: messages.en.Messages
):
    await state.clear()
    tg_id = message.chat.id
    has_code = await ChatCode.objects.filter(tg_user_id=tg_id).aexists()
    if not has_code:
        await message.reply(m.delete_link_no_link, reply_markup=ReplyKeyboardRemove())
    else:
        await state.set_state(DeletionStates.requested)
        await message.reply(
            m.delete_link_confirmation,
            reply_markup=confirmation_keyboard(yes=m.yes_delete, no=m.no_cancel),
        )


@dp.message(DeletionStates.requested, F.text.in_(messages.union.yes_delete))
async def delete_code_confirmed(
    message: types.Message, state: FSMContext, m: messages.en.Messages
):
    tg_id = message.chat.id
    await ChatCode.objects.filter(tg_user_id=tg_id).adelete()
    await state.clear()
    await message.reply(m.delete_link_deleted, reply_markup=ReplyKeyboardRemove())


@dp.message(DeletionStates.requested, F.text.in_(messages.union.no_cancel))
async def delete_code_not_confirmed(
    message: types.Message, state: FSMContext, m: messages.en.Messages
):
    await state.clear()
    await message.reply(m.delete_link_cancelled, reply_markup=ReplyKeyboardRemove())


@dp.message(DeletionStates.requested)
async def unknown(message: types.Message, m: messages.en.Messages):
    await message.reply(m.confirmation_keyboard_ignored)
