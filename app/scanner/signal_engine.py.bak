import pandas as pd

from app.scanner.indicators import (
    trend_score,
    volume_score,
    momentum_score,
    liquidity_score,
    relative_strength_score
)

from app.scanner.scoring import (
    calculate_score,
    confidence
)

from app.risk.trade_plan import build_trade_plan


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
        momentum = momentum_score(df)
        liquidity = liquidity_score(df)
        rs = relative_strength_score(df)

        score = calculate_score(
            trend,
            volume,
            rs,
            liquidity,
            momentum
        )

        conf = confidence(score)

        plan = build_trade_plan(df)

        return {
            "symbol": symbol,
            "score": score,
            "confidence": conf,
            "trend": trend,
            "volume": volume,
            "momentum": momentum,
            "liquidity": liquidity,
            "entry": plan["entry"],
            "sl": plan["sl"],
            "tp1": plan["tp1"],
            "tp2": plan["tp2"],
            "tp3": plan["tp3"],
            "rr": plan["rr"]
        }
