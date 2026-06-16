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

    def get_top_futures(self, limit=100):

        markets = self.exchange.load_markets()

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

        return pairs[:limit]
