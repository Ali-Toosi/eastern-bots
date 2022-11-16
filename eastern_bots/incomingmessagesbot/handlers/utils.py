from django.conf import settings
from django.urls import reverse

from eastern_bots.incomingmessagesbot.models import ChatWebhook


def get_webhook_url(webhook: ChatWebhook):
    return f"https://{settings.DOMAIN_NAME}" + reverse(
        "incomingmessagesbot:incoming_message_webhook", args=(webhook.token,)
    )
