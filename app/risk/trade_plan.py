def build_trade_plan(df):

    entry = float(df["close"].iloc[-1])

    high = df["high"]
    low = df["low"]

    tr = (high - low).abs()

    atr = tr.rolling(14).mean().iloc[-1]

    if atr <= 0:
        atr = entry * 0.01

    sl = entry - (atr * 1.5)

    risk = entry - sl

    tp1 = entry + risk * 2
    tp2 = entry + risk * 3
    tp3 = entry + risk * 5

    return {
        "entry": round(entry, 8),
        "sl": round(sl, 8),
        "tp1": round(tp1, 8),
        "tp2": round(tp2, 8),
        "tp3": round(tp3, 8),
        "rr": "1:5"
    }
