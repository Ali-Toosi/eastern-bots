from aiogram import Bot, F, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State
from aiogram.types import ReplyKeyboardRemove

from ...utils.common_keyboards import confirmation_keyboard
from .. import messages as m
from ..bot import dp
from ..models import Blocked

confirmation_state = State("confirm_block")


@dp.callback_query(lambda callback_query: str(callback_query.data).startswith("block_"))
async def block_request(
    callback_query: types.CallbackQuery, state: FSMContext, bot: Bot
):
    user_tg_id = callback_query.message.chat.id
    dst_tg_id = callback_query.data.split("_")[1]
    await callback_query.answer()
    await state.set_state(confirmation_state)
    await state.set_data({"blocking": dst_tg_id})
    await bot.send_message(
        user_tg_id,
        m.block_confirmation,
        reply_markup=confirmation_keyboard(yes="Yes, block!"),
    )


@dp.message(confirmation_state, F.text == "Yes, block!")
async def block_confirmed(message: types.Message, state: FSMContext):
    user_tg_id = message.chat.id
    dst_tg_id = (await state.get_data())["blocking"]
    _, __ = await Blocked.objects.aget_or_create(blocker=user_tg_id, blocked=dst_tg_id)
    await state.clear()
    await message.reply(m.user_blocked, reply_markup=ReplyKeyboardRemove())


@dp.message(confirmation_state, F.text == "No, cancel.")
async def block_cancelled(message: types.Message, state: FSMContext):
    await state.clear()
    await message.reply(m.block_cancelled, reply_markup=ReplyKeyboardRemove())


@dp.message(confirmation_state)
async def unknown(message: types.Message):
    await message.reply("I didn't get that. Use the keyboard:")
