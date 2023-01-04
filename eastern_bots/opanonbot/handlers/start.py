from aiogram import types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

from .. import messages as m
from ..bot import dp


@dp.message(Command(commands=["start"]))
async def start(message: types.Message, state: FSMContext):
    await state.clear()
    await message.reply(
        m.start_message, reply_markup=ReplyKeyboardRemove(), parse_mode="markdown"
    )


@dp.message(Command(commands=["help"]))
async def tips(message: types.Message, state: FSMContext):
    await state.clear()
    await message.reply(
        m.help_message,
        reply_markup=ReplyKeyboardRemove(),
        parse_mode="markdown",
        disable_web_page_preview=True,
    )
