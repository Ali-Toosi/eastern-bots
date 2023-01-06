from aiogram import Bot, F, types
from aiogram.exceptions import TelegramAPIError
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove

from .. import messages
from ..bot import dp
from ..models import ChatCode
from ..utils import anon_message_reply_markup, chat_code_is_valid, user_is_not_blocked


class ChatStates(StatesGroup):
    awaiting_message = State()


@dp.message(Command(commands=["start"]), F.text.contains(" C"))
async def check_code(
    message: types.Message, state: FSMContext, bot: Bot, m: messages.en.Messages
):
    # Came here from /start
    code = message.text.split(" C")[1]

    tg_id = str(message.chat.id)
    if not await chat_code_is_valid(bot, m, code, tg_id):
        await state.clear()
        return

    dst_tg_id = (await ChatCode.objects.aget(code=code)).tg_user_id
    if dst_tg_id == tg_id:
        await message.reply(m.no_self_messaging, reply_markup=ReplyKeyboardRemove())
        return

    await state.set_state(ChatStates.awaiting_message)
    await state.set_data({"recipient": dst_tg_id})
    await message.reply(m.send_ask_message, reply_markup=ReplyKeyboardRemove())


@dp.message(ChatStates.awaiting_message)
async def received_anon_message(
    message: types.Message, state: FSMContext, bot: Bot, m: messages.en.Messages
):
    user_tg_id = message.chat.id
    state_data = await state.get_data()
    dst_tg_id = state_data["recipient"]
    reply_to_message_id = state_data.get("reply_to")

    try:
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
    except TelegramAPIError:
        await message.reply(m.send_failed)

    await state.clear()
    await message.reply(m.send_successful)


@dp.callback_query(lambda callback_query: str(callback_query.data).startswith("reply_"))
async def reply_request(
    callback_query: types.CallbackQuery,
    state: FSMContext,
    bot: Bot,
    m: messages.en.Messages,
):
    user_tg_id = callback_query.message.chat.id
    dst_tg_id, message_id = callback_query.data.split("_")[1:]
    await callback_query.answer()

    if not await user_is_not_blocked(bot, m, dst_tg_id, user_tg_id):
        return

    await state.set_state(ChatStates.awaiting_message)
    await state.set_data({"recipient": dst_tg_id, "reply_to": message_id})
    await bot.send_message(
        user_tg_id, m.send_ask_message, reply_markup=ReplyKeyboardRemove()
    )
