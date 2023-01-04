from aiogram import types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

from eastern_bots.incomingmessagesbot.messages import (
    cancel_message,
    help_message,
    start_message,
)

from ..bot import dp


@dp.message(Command(commands=["start"]))
async def start(message: types.Message, state: FSMContext):
    await state.clear()
    await message.reply(
        start_message, reply_markup=ReplyKeyboardRemove(), parse_mode="markdown"
    )


@dp.message(Command(commands=["help"]))
async def help_command(message: types.Message, state: FSMContext):
    await state.clear()
    await message.reply(
        help_message,
        parse_mode="markdown",
        reply_markup=ReplyKeyboardRemove(),
        disable_web_page_preview=True,
    )


@dp.message(Command(commands=["cancel"]))
async def cancel_command(message: types.Message, state: FSMContext):
    await state.clear()
    await message.reply(cancel_message, reply_markup=ReplyKeyboardRemove())
