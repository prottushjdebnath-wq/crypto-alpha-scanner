import json


class TradeStats:

    def __init__(self):
        self.file = "data/trades.jsonl"

    def summary(self):

        wins = 0
        losses = 0
        open_trades = 0

        try:

            with open(self.file, "r") as f:

                for line in f:

                    trade = json.loads(line)

                    status = trade.get("status", "OPEN")

                    if status == "WIN":
                        wins += 1

                    elif status == "LOSS":
                        losses += 1

                    else:
                        open_trades += 1

        except:
            pass

        total_closed = wins + losses

        winrate = (
            round(wins * 100 / total_closed, 2)
            if total_closed > 0 else 0
        )

        return {
            "wins": wins,
            "losses": losses,
            "open": open_trades,
            "winrate": winrate
        }
