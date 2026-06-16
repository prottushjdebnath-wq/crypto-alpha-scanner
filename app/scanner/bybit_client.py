import ccxt

class BybitClient:
    def __init__(self):
        self.exchange = ccxt.bybit({
            "enableRateLimit": True
        })

    def get_ticker(self, symbol):
        return self.exchange.fetch_ticker(symbol)

    def get_ohlcv(self, symbol, timeframe="1h", limit=250):
        return self.exchange.fetch_ohlcv(
            symbol,
            timeframe=timeframe,
            limit=limit
        )

    def get_markets(self):
        return self.exchange.load_markets()
