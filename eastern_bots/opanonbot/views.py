import asyncio
import json

from asgiref.sync import async_to_sync
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .bot import dp, get_bot_instance


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
