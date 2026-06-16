def build_trade_plan(df):

    entry = float(df["close"].iloc[-1])

    atr = (
        df["high"].tail(14).max()
        -
        df["low"].tail(14).min()
    ) / 14

    sl = entry - (atr * 2)

    risk = entry - sl

    tp1 = entry + risk * 1.5
    tp2 = entry + risk * 3
    tp3 = entry + risk * 5

    return {
        "entry": round(entry, 4),
        "sl": round(sl, 4),
        "tp1": round(tp1, 4),
        "tp2": round(tp2, 4),
        "tp3": round(tp3, 4),
        "rr": "1:5"
    }
