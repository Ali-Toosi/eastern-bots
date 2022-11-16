import re

from aiogram import types
from aiogram.filters import Command

from ..bot import dp
from ..models import ChatWebhook, TelegramChat
from .utils import get_webhook_url


@dp.message(Command(re.compile(r"link_\d+")))
async def show_webhook_link(message: types.Message, chat: TelegramChat):
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

    webhook_url = get_webhook_url(webhook)
    response = f"Here you go:\n{webhook_url}\n\nIf you need help with using the webhook press /help."

    await message.reply(response)
