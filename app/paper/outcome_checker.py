import json

from app.scanner.bybit_client import BybitClient


class OutcomeChecker:

    def __init__(self):
        self.file = "data/trades.jsonl"
        self.client = BybitClient()

    def run(self):

        updated = []

        try:

            with open(self.file, "r") as f:
                trades = [json.loads(x) for x in f]

        except:
            return []

        for trade in trades:

            if trade.get("status") != "OPEN":
                updated.append(trade)
                continue

            try:

                ticker = self.client.get_ticker(
                    trade["symbol"]
                )

                price = ticker["last"]

                if price >= trade["take_profit"]:

                    trade["status"] = "WIN"
                    trade["exit_price"] = price

                elif price <= trade["stop_loss"]:

                    trade["status"] = "LOSS"
                    trade["exit_price"] = price

            except:
                pass

            updated.append(trade)

        with open(self.file, "w") as f:

            for trade in updated:
                f.write(
                    json.dumps(trade) + "\n"
                )

        return updated
