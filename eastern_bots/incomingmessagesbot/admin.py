from django.contrib import admin

from eastern_bots.incomingmessagesbot.models import (
    ChatWebhook,
    TelegramChat,
    TelegramUser,
)

# Register your models here.

admin.site.register([TelegramUser, TelegramChat, ChatWebhook])
