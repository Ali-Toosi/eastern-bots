from aiogram.types import ForceReply, KeyboardButton, ReplyKeyboardMarkup


def confirmation_keyboard(
    yes="Yes!", no="No, cancel.", resize_keyboard=True, selective=True
):
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=yes), KeyboardButton(text=no)]],
        resize_keyboard=resize_keyboard,
        selective=selective,
    )


def force_reply(placeholder=None, selective=True):
    return ForceReply(input_field_placeholder=placeholder, selective=selective)
