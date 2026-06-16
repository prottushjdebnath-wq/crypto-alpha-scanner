import asyncio

from app.telegram.notifier import TelegramNotifier
from app.config.settings import BOT_TOKEN, CHAT_ID

async def main():

    notifier = TelegramNotifier(BOT_TOKEN)

    await notifier.send(
        CHAT_ID,
        "🚀 Telegram test successful"
    )

asyncio.run(main())
