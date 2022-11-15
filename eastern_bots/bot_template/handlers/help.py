from aiogram import types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State

from ..bot import dp


@dp.message(Command(commands=["start"]))
async def start(message: types.Message, state: FSMContext):
    await state.set_state(State("started"))
    await state.set_data({"key123": "data"})
    await message.reply("Hey")


@dp.message(State("started"))
async def good(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await state.clear()
    await message.reply(data["key123"])
