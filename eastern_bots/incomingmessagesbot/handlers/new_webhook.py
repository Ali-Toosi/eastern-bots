from aiogram import F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove
from django.utils.crypto import get_random_string

from eastern_bots.utils.common_keyboards import confirmation_keyboard, force_reply

from ..bot import dp
from ..models import ChatWebhook, TelegramChat, TelegramUser
from .utils import get_webhook_url


class States(StatesGroup):
    started = State()
    waiting_for_confirmation = State()


@dp.message(Command(commands=["new"]))
async def new_command(message: types.Message, state: FSMContext):
    await state.set_state(States.started)
    await message.reply(
        "Choose a name for the webhook so you can find it later (make sure you reply to this message) or /cancel:",
        reply_markup=force_reply(),
    )


@dp.message(States.started)
async def name_chosen(message: types.Message, state: FSMContext):
    chosen_name = message.text
    if chosen_name in [None, ""]:
        await message.reply("Name should be text. Try again (or /cancel):")
        return

    if len(chosen_name) > 128:
        await message.reply(
            "Name can't be longer than 128 characters. Try again (or /cancel):"
        )
        return

    await state.set_state(States.waiting_for_confirmation)
    await state.set_data({"name": chosen_name})
    await message.reply(
        "Got it. The webhook will be created for this chat. That means everytime you call it, I will send "
        "a message here. Confirm?",
        reply_markup=confirmation_keyboard(),
    )


@dp.message(States.waiting_for_confirmation, F.text == "Yes!")
async def confirmed(
    message: types.Message, state: FSMContext, chat: TelegramChat, user: TelegramUser
):
    webhook_name = (await state.get_data())["name"]
    token = None
    while not token:
        token = get_random_string(8)
        if await ChatWebhook.objects.filter(token=token).aexists():
            token = None

    webhook = await ChatWebhook.objects.acreate(
        tg_user=user, tg_chat=chat, title=webhook_name, token=token
    )
    webhook_url = get_webhook_url(webhook)
    await state.clear()
    await message.answer(
        f"Done! Your webhook is available at:\n{webhook_url}",
        reply_markup=ReplyKeyboardRemove(),
    )


@dp.message(States.waiting_for_confirmation, F.text == "No, cancel.")
async def not_confirmed(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "Well, let me know if you change your mind!",
        reply_markup=ReplyKeyboardRemove(),
    )


@dp.message(States.waiting_for_confirmation)
async def unknown_confirmation(message: types.Message):
    await message.reply("I didn't get that. Use the keyboard:")
