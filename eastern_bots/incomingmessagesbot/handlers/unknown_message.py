from aiogram import types

from ..bot import dp


@dp.message()
async def unknown(message: types.Message):
    await message.answer("Mm hmm")
