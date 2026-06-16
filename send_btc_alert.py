import asyncio

from app.scanner.bybit_client import BybitClient
from app.telegram.notifier import TelegramNotifier
from app.config.settings import CHAT_ID

async def main():

    client = BybitClient()
    notifier = TelegramNotifier()

    ticker = client.get_ticker("BTC/USDT:USDT")

    message = f"""
🚀 Scanner Online

Symbol: BTCUSDT

Price: {ticker['last']}
24H Volume: {ticker.get('quoteVolume')}

Source: Bybit Futures
"""

    await notifier.send(CHAT_ID, message)

asyncio.run(main())
