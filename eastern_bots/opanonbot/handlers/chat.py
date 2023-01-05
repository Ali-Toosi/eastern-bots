from aiogram import Bot, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove

from .. import messages as m
from ..bot import dp
from ..models import ChatCode
from ..utils import anon_message_reply_markup, chat_code_is_valid, user_is_not_blocked


class ChatStates(StatesGroup):
    asked_code = State()
    awaiting_message = State()


@dp.message(Command(commands=["send"]))
async def start_sending(message: types.Message, state: FSMContext):
    await state.set_state(ChatStates.asked_code)
    await message.reply(m.send_ask_code, reply_markup=ReplyKeyboardRemove())


@dp.message(ChatStates.asked_code)
async def check_code(message: types.Message, state: FSMContext, bot: Bot):
    code = message.text
    tg_id = message.chat.id
    if not await chat_code_is_valid(bot, code, tg_id):
        await state.clear()
        return

    dst_tg_id = (await ChatCode.objects.aget(code=code)).tg_user_id
    await state.set_state(ChatStates.awaiting_message)
    await state.set_data({"recipient": dst_tg_id})
    await message.reply(m.send_ask_message, reply_markup=ReplyKeyboardRemove())


@dp.message(ChatStates.awaiting_message)
async def received_anon_message(message: types.Message, state: FSMContext, bot: Bot):
    user_tg_id = message.chat.id
    state_data = await state.get_data()
    dst_tg_id = state_data["recipient"]
    reply_to_message_id = state_data.get("reply_to")

    if not reply_to_message_id:
        reply_to_message_id = (
            await bot.send_message(dst_tg_id, m.new_anonymous_chat)
        ).message_id
    await bot.copy_message(
        dst_tg_id,
        user_tg_id,
        message.message_id,
        reply_to_message_id=reply_to_message_id,
        reply_markup=anon_message_reply_markup(user_tg_id, message.message_id),
    )

    await state.clear()
    await message.reply(m.send_successful, reply_markup=ReplyKeyboardRemove())


@dp.callback_query(lambda callback_query: str(callback_query.data).startswith("reply_"))
async def reply_request(
    callback_query: types.CallbackQuery, state: FSMContext, bot: Bot
):
    user_tg_id = callback_query.message.chat.id
    dst_tg_id, message_id = callback_query.data.split("_")[1:]
    await callback_query.answer()

    if not await user_is_not_blocked(bot, dst_tg_id, user_tg_id):
        return

    await state.set_state(ChatStates.awaiting_message)
    await state.set_data({"recipient": dst_tg_id, "reply_to": message_id})
    await bot.send_message(
        user_tg_id, m.send_ask_message, reply_markup=ReplyKeyboardRemove()
    )
