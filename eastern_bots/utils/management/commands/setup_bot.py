from importlib import import_module

from aiogram import Bot
from asgiref.sync import async_to_sync
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = (
        "Sets up the token and commands of a bot to match the bot app in this project"
    )

    def handle(self, *args, **options):
        bot_token = input("Enter bot token: ").strip()
        base_url = input("Base URL for the webhook (with https): ").strip()
        if base_url[-1] == "/":
            base_url = base_url[:-1]
        app_name = input("Name of the app in project: ").lower().strip()

        bot_username = async_to_sync(Bot(bot_token).get_me)().username

        webhook_url = f"{base_url}/{app_name}/webhook/{bot_token}/"
        async_to_sync(Bot(bot_token).set_webhook)(webhook_url)
        self.stdout.write(
            self.style.SUCCESS('Successfully set webhook for "%s"' % bot_username)
        )

        try:
            commands_module = import_module(f"eastern_bots.{app_name}.commands")
            commands = commands_module.bot_map[bot_username.lower()]
        except (ImportError, ValueError, AttributeError) as e:
            print(repr(e))
            commands = None
        if commands:
            async_to_sync(Bot(bot_token).set_my_commands)(commands)
            self.stdout.write(
                self.style.SUCCESS('Successfully set commands for "%s"' % bot_username)
            )
