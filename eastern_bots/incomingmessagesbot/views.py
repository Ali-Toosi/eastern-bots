import asyncio
import json

from asgiref.sync import async_to_sync, sync_to_async
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .bot import dp, get_bot_instance, get_default_bot
from .models import ChatWebhook


def heartbeat(request):
    return HttpResponse("I'm OK.")


@csrf_exempt
@async_to_sync
async def bot_webhook(request, token):
    update = json.loads(request.body.decode("utf-8"))
    bot = await get_bot_instance(token)
    if not bot:
        return HttpResponse("Bot not registered.")

    # Run in the background
    # asyncio.create_task(dp.feed_raw_update(bot, update))

    # Or wait for execution
    try:
        await dp.feed_raw_update(bot, update)
    except Exception as e:
        # Catching "Exception" is the worst. But there is no option. If the code fails, the webhook shouldn't fail.
        # If the webhook fails Telegram will stop sending messages altogether. Best solution is to catch all possible
        # exceptions in your handlers and log any that reach here.
        if settings.DEBUG:
            raise e

    return HttpResponse("OK.")


@async_to_sync
async def poll_bot_updates(request, token):
    if not settings.DEBUG:
        return HttpResponse("Not allowed.")

    bot = await get_bot_instance(token)
    if not bot:
        return HttpResponse("Bot not registered.")

    asyncio.create_task(dp.start_polling(bot))
    return HttpResponse("OK.")


@csrf_exempt
@async_to_sync
async def incoming_message(request, token):
    """
    This view handles the endpoint you can call to send messages to your webhook.

    It only supports text messages right now. The webhook token should be in the url
    and the text message to send should be in the Post request with key ``message``.

    The full URL to this endpoint should be given to the user in the bot, so they
    won't have to add the token to the URL manually.

    :param request: The HTTP request
    :param token: The webhook token extracted from the URL
    :return:
        404 error if the passed token does not exist.
        400 error if the ``message`` key does not exist in `post` request.
        Otherwise, the message will be sent to the Telegram chat and 200 response
        will be returned.
    """
    webhook: ChatWebhook = await sync_to_async(get_object_or_404)(
        ChatWebhook, token=token
    )
    text = request.POST.get("message", None)
    if text is None:
        return HttpResponse("Empty message.", status=400)

    @sync_to_async
    def get_telegram_id():
        return webhook.tg_chat.telegram_id

    bot = await get_default_bot()
    await bot.send_message(await get_telegram_id(), text)
    return HttpResponse("OK")
