from textwrap import dedent

from . import en

language = "fa"


class Messages(en.Messages):
    command_start = "شروع و دیدن دستورها"
    command_help = "کمک در استفاده از ربات"
    command_send = "ارسال پیام ناشناس"
    command_receive = "دریافت پیام ناشناس"
    command_new_code = "دریافت لینک ناشناس جدید"
    command_delete_code = "حذف لینک ناشناس"

    start_message = dedent(
        """\
        *ارسال پیام ناشناس*
        روی /send کلیک کن، کد طرف رو وارد کن و ناشناس پیام بده!

        *دریافت پیام ناشناس*
        روی /receive کلیک کن، کد یا لینک ناشناست رو بگیر و بده به بقیه!

        هر وقت خسته شدی میتونی با /delete\\_code لینکت رو پاک کنی یا با /new\\_code یه لینک جدید بگیری.

        *راهنما*
        روی /help بزن تا یه سری نکته کمکی بگیری.
    """
    )

    help_message = (
        "*ادمین ربات پیام‌های من رو می‌بینه؟*" + "\n"
        "نه. همه چیز ناشناس و کد این ربات هم متن بازه. می‌تونین کد ربات رو اینجا ببینین:"
        + "\n"
        "[کد در گیت‌هاب](https://github.com/Ali-Toosi/eastern-bots/tree/main/eastern_bots/opanonbot) "
        "\n\n"
        "*چطوری یکی رو آنبلاک کنم؟*" + "\n"
        "متاسفانه وقتی یکی رو بلاک کنی دیگه نمی‌تونی آنبلاکش کنی."
        "\n\n"
        "*فرق کد با لینک چیه؟*" + "\n"
        "فرق خاصی ندارن. اگه کسی لینک داشته باشه میتونه مستقیم کلیک کنه بیاد تو چت. اگه کد داشته باشه اول باید بزنه"
        "/send بعد کد رو بده بعد چت رو شروع کنه"
        "\n\n"
        "*میشه به ربات امکانات اضافه کرد؟*" + "\n"
        "بله میشه. این ربات اوپن‌سورس هست و اگه برنامه‌نویسی بلدین "
        "و می‌خواین امکانی به ربات اضافه کنین خیلی استقبال میشه."
        "\nhttps://github.com/Ali-Toosi/eastern-bots"
    )

    show_code = dedent(
        """\
        این کد ناشناس شماست: `{code}` (کلیک کن کپی میشه).

        هر کسی این کد رو داشته باشه می‌تونه بهت پیام بده مگه اینکه بلاک باشه.

        می‌تونی کدت رو با /delete\\_code پاک کنی یا با /new\\_code یه کد جدید بگیری.

        اینم لینک ناشناست:
    """
    )

    delete_code_no_code = "کد و لینک ناشناسی برای پاک کردن نداری. میتونی با /receive یه کد ناشناس برای خودت بگیری."
    delete_code_confirmation = "مطمئنی می‌خوای کدت رو پاک کنی؟ هیچ کس دیگه نمیتونه با این کد و لینک بهت پیام بده"
    delete_code_deleted = (
        "لینک ناشناست پاک شد! اگر خواستی می‌تونی با /receive یه لینک جدید بگیری."
    )
    delete_code_cancelled = "حله."

    new_code_confirmation = dedent(
        """\
        درست کردن لینک جدید، لینک قبلیت رو حذف می‌کنه و دیگه ازش پیامی نمی‌گیری.

        مطمئنی می‌خوای لینک جدید درست کنی؟
    """
    )
    new_code_created = (
        "کد ناشناس جدیدت: `{code}` (کلیک کن کپی میشه)" + "\n" "اینم لینک جدیدت:"
    )

    send_ask_code = "کد ناشناسی که می‌خوای باهاش چت کنی رو بفرست:"
    send_code_not_found = "این کد وجود نداره. می‌تونی دوباره امتحان کنی 👈 /send"
    send_blocked = "متاسفانه بلاک شدی و نمی‌تونی به این آدم پیام بدی 😞"
    send_ask_message = "پیام ناشناست رو بفرست تا بفرستم..."
    send_successful = "فرستادم براش! هر وقت جواب بده بهت خبر میدم"
    send_failed = (
        "پیامت ارسال نشد! با یه پیام دیگه امتحان کن. اگه بازم ارسال نشد یعنی احتمالا دیگه از این ربات استفاده نمیکنه"
        " و نمی‌تونه پیامی دریافت کنه."
    )

    new_anonymous_chat = "چت ناشناس حدید!"

    block_confirmation = "مطمئنی می‌خوای بلاک کنی؟ دیگه هیچ پیامی ازش نمی‌گیری!"
    user_blocked = "بلاک شد! تمام!"
    block_cancelled = "ردیفه. بلاک نمی‌کنم : )"

    unknown_message = "نمی‌دونم این پیام چیه 🤷‍♀️"
    confirmation_keyboard_ignored = "نفهمیدم! بی‌زحمت از کیبورد استفاده کن:"

    yes_delete = "آره پاک کن"
    no_cancel = "نه! لغو"
    yes_do_it = "آره!"
    yes_block = "قطعا بلاک!"