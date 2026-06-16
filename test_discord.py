import asyncio

from app.telegram.notifier import TelegramNotifier
from app.config.settings import BOT_TOKEN

async def main():

    notifier = TelegramNotifier(BOT_TOKEN)

    await notifier.send(
        "discord",
        "🚀 Discord test successful"
    )

asyncio.run(main())
