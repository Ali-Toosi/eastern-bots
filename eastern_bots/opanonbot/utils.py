import string

from asgiref.sync import sync_to_async
from django.utils.crypto import get_random_string

from eastern_bots.opanonbot.models import ChatCode


async def create_new_chat_code(tg_user_id):
    """
    Create a new unique code for this Telegram id and save it on ChatCode.
    :param tg_user_id: The Telegram id for which we want to create a new chat code.
    :return: The new chat code (not the object, the code itself).
    """
    chat_code, _ = await ChatCode.objects.aget_or_create(tg_user_id=tg_user_id)
    code = None
    while not code:
        code = get_random_string(
            5, allowed_chars=string.ascii_lowercase + string.digits
        )
        if await ChatCode.objects.filter(code=code).aexists():
            code = None
    chat_code.code = code
    await sync_to_async(chat_code.save)()
    return code
