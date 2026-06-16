import json
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
