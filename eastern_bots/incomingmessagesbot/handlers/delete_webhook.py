import re

from aiogram import F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State
from aiogram.types import ReplyKeyboardRemove

from eastern_bots.utils.common_keyboards import confirmation_keyboard

from ..bot import dp
from ..models import ChatWebhook, TelegramChat


@dp.message(Command(re.compile(r"delete_\d+")))
async def delete_webhook(message: types.Message, chat: TelegramChat, state: FSMContext):
    try:
        webhook_id = int(message.text.split("_")[-1])
    except ValueError:
        await message.reply("I don't... understand this :/")
        return

    try:
        webhook = await ChatWebhook.objects.aget(id=webhook_id, tg_chat=chat)
    except ChatWebhook.DoesNotExist:
        await message.reply("This webhook does not exist!")
        return

    response = (
        f"You are about to delete this webhook: *{webhook.title}*.\nAre you sure?"
    )

    await state.set_state(State("confirm"))
    await state.set_data({"webhook_id": webhook_id})
    await message.reply(
        response, reply_markup=confirmation_keyboard(), parse_mode="markdown"
    )


@dp.message(State("confirm"), F.text == "Yes!")
async def confirmed(message: types.Message, state: FSMContext):
    webhook_id = (await state.get_data())["webhook_id"]
    await ChatWebhook.objects.filter(id=webhook_id).adelete()
    await state.clear()
    await message.reply("Webhook deleted.", reply_markup=ReplyKeyboardRemove())


@dp.message(State("confirm"), F.text == "No, cancel.")
async def not_confirmed(message: types.Message, state: FSMContext):
    await state.clear()
    await message.reply("No deletions today : )", reply_markup=ReplyKeyboardRemove())


@dp.message(State("confirm"))
async def unknown(message: types.Message):
    await message.reply("I didn't get that. Use the keyboard or /cancel")
