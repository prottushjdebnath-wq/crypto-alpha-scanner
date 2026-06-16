import json


class ResultEngine:

    def __init__(self):
        self.trades_file = "data/trades.jsonl"

    def stats(self):

        wins = 0
        losses = 0
        total = 0

        try:

            with open(self.trades_file, "r") as f:

                for line in f:

                    trade = json.loads(line)

                    if trade.get("status") == "WIN":
                        wins += 1

                    if trade.get("status") == "LOSS":
                        losses += 1

            total = wins + losses

            if total == 0:
                winrate = 0
            else:
                winrate = round((wins / total) * 100, 2)

            return {
                "wins": wins,
                "losses": losses,
                "total": total,
                "winrate": winrate
            }

        except Exception:

            return {
                "wins": 0,
                "losses": 0,
                "total": 0,
                "winrate": 0
            }
