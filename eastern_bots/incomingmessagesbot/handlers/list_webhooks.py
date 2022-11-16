from aiogram import types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from asgiref.sync import sync_to_async

from ..bot import dp
from ..models import ChatWebhook, TelegramChat


@dp.message(Command(commands=["list"]))
async def new_command(message: types.Message, state: FSMContext, chat: TelegramChat):
    await state.clear()
    webhooks = ChatWebhook.objects.filter(tg_chat=chat).prefetch_related(
        "tg_user", "tg_chat"
    )

    response = (
        "Here are all of the webhooks in this chat. Click on `delete` or `link` to "
        "delete the webhook or to show its URL again:\n\n"
    )

    @sync_to_async
    def get_first_100():
        return list(webhooks[:100])

    @sync_to_async
    def get_creator_name(single_webhook):
        username = single_webhook.tg_user.username
        if username:
            return f"[{single_webhook.tg_user.first_name}](https://t.me/{username})"
        else:
            return (
                single_webhook.tg_user.first_name
                + " "
                + single_webhook.tg_user.last_name
            )

    webhooks = await get_first_100()
    for webhook in webhooks:
        creator_name = await get_creator_name(webhook)
        response += f"*{webhook.title}* - created by {creator_name}\n"
        response += (
            rf"/link\_{str(webhook.id)} to see the link or, /delete\_{str(webhook.id)}"
        )
        response += "\n\n"

    if len(webhooks) == 0:
        response += "No webhooks created yet."

    await message.reply(response, parse_mode="markdown", disable_web_page_preview=True)
