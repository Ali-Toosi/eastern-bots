from aiogram import types

from .. import messages
from ..bot import dp


@dp.message()
async def unknown_message(message: types.Message, m: messages.en.Messages):
    await message.reply(m.unknown_message)
