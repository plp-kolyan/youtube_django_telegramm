from django.core.management.base import BaseCommand
from telethon.sync import TelegramClient, events
from serveses_config import api_id, api_hash, bot_token
from simplebot.models import Answer


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        bot = TelegramClient('bot',
                api_id, api_hash).start(
            bot_token=bot_token)

        with bot:
            @bot.on(events.NewMessage())
            async def message_handler(event):
                answer = await Answer.objects.aget(
                    command=event.message.message
                )
                await event.reply(
                    answer.text
                )


            bot.run_until_disconnected()
