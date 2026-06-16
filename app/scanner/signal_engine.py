import pandas as pd

from app.scanner.indicators import (
    trend_score,
    volume_score
)

from app.scanner.scoring import calculate_score

class SignalEngine:

    def evaluate(self, symbol, ohlcv):

        df = pd.DataFrame(
            ohlcv,
            columns=[
                "timestamp",
                "open",
                "high",
                "low",
                "close",
                "volume"
            ]
        )

        trend = trend_score(df)
        volume = volume_score(df)

        score = calculate_score(
            trend,
            volume,
            30
        )

        return {
            "symbol": symbol,
            "score": score
        }
