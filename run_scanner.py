import asyncio

from app.scanner.bybit_client import BybitClient
from app.scanner.signal_engine import SignalEngine
from app.telegram.notifier import TelegramNotifier
from app.config.settings import BOT_TOKEN, CHAT_ID

PAIRS = [
    "BTC/USDT:USDT",
    "ETH/USDT:USDT",
    "SOL/USDT:USDT",
    "SUI/USDT:USDT",
    "DOGE/USDT:USDT",
    "APT/USDT:USDT"
]

async def main():

    client = BybitClient()
    engine = SignalEngine()
    notifier = TelegramNotifier(BOT_TOKEN)

    results = []

    for symbol in PAIRS:

        try:
            ohlcv = client.get_ohlcv(
                symbol,
                timeframe="1h",
                limit=250
            )

            signal = engine.evaluate(
                symbol,
                ohlcv
            )

            results.append(signal)

        except Exception as e:
            print(symbol, e)

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    message = "🔥 TOP SCANNER RESULTS\n\n"

    for i, item in enumerate(results[:5], start=1):
        message += (
            f"{i}. {item['symbol']}\n"
            f"Score: {item['score']}\n\n"
        )

    print(message)

    await notifier.send(
        CHAT_ID,
        message
    )

asyncio.run(main())
