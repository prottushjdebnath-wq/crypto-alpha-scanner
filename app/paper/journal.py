import json
from datetime import datetime

def log_trade(symbol, side, score, entry):

    trade = {
        "time": str(datetime.utcnow()),
        "symbol": symbol,
        "side": side,
        "score": score,
        "entry": entry
    }

    with open("data/trades.jsonl", "a") as f:
        f.write(json.dumps(trade) + "\n")
