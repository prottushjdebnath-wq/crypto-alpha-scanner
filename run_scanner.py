import asyncio

from app.scanner.bybit_client import BybitClient
from app.scanner.signal_engine import SignalEngine
from app.telegram.notifier import TelegramNotifier
from app.paper.tracker import PaperTracker
from app.config.settings import BOT_TOKEN, CHAT_ID


async def main():

    client = BybitClient()
    engine = SignalEngine()
    notifier = TelegramNotifier(BOT_TOKEN)
    tracker = PaperTracker()

    markets = client.get_markets()

    pairs = []

    for symbol, market in markets.items():

        try:

            if (
                market.get("active")
                and market.get("swap")
                and market.get("quote") == "USDT"
            ):
                pairs.append(symbol)

        except:
            pass

    print(f"Scanning {len(pairs)} futures pairs")

    results = []

    for symbol in pairs[:100]:

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

            tracker.record(
                signal["symbol"],
                "LONG",
                signal["score"],
                signal["entry"],
                signal["sl"],
                signal["tp1"]
            )

        except Exception as e:
            print(symbol, e)

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    top = results[:10]

    message = "🚀 TOP FUTURES OPPORTUNITIES\n\n"

    for i, item in enumerate(top, start=1):

        message += (
            f"#{i} {item['symbol']}\n"
            f"Score: {item['score']}\n"
            f"Entry: {item['entry']}\n"
            f"SL: {item['sl']}\n"
            f"TP1: {item['tp1']}\n"
            f"TP2: {item['tp2']}\n"
            f"TP3: {item['tp3']}\n"
            f"RR: {item['rr']}\n\n"
        )

    print(message)

    await notifier.send(
        CHAT_ID,
        message
    )


asyncio.run(main())
