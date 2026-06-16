import json
import os
from datetime import datetime


class PaperTracker:

    def __init__(self):
        self.file = "data/trades.jsonl"

    def record(
        self,
        symbol,
        side,
        score,
        entry,
        stop_loss,
        take_profit
    ):

        if os.path.exists(self.file):

            with open(self.file, "r") as f:

                for line in f:

                    try:

                        trade = json.loads(line)

                        if (
                            trade["symbol"] == symbol
                            and trade["status"] == "OPEN"
                        ):
                            return

                    except:
                        pass

        trade = {
            "timestamp": datetime.utcnow().isoformat(),
            "symbol": symbol,
            "side": side,
            "score": score,
            "entry": entry,
            "stop_loss": stop_loss,
            "take_profit": take_profit,
            "status": "OPEN"
        }

        with open(self.file, "a") as f:
            f.write(json.dumps(trade) + "\n")
