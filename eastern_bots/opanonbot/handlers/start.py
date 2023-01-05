from aiogram import F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

from .. import messages
from ..bot import dp


@dp.message(Command(commands=["start"]), ~F.text.contains(" C"))
async def start(message: types.Message, state: FSMContext, m: messages.en.Messages):
    await state.clear()
    await message.reply(
        m.start_message, reply_markup=ReplyKeyboardRemove(), parse_mode="markdown"
    )


@dp.message(Command(commands=["help"]))
async def tips(message: types.Message, state: FSMContext, m: messages.en.Messages):
    await state.clear()
    await message.reply(
        m.help_message,
        reply_markup=ReplyKeyboardRemove(),
        parse_mode="markdown",
        disable_web_page_preview=True,
    )


@dp.message()
async def unknown_message(message: types.Message, m: messages.en.Messages):
    await message.reply(m.unknown_message)
