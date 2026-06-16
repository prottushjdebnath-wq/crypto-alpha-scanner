import pandas as pd

def ema(series, period):
    return series.ewm(span=period, adjust=False).mean()

def trend_score(df):
    df["ema50"] = ema(df["close"], 50)
    df["ema200"] = ema(df["close"], 200)

    if df["ema50"].iloc[-1] > df["ema200"].iloc[-1]:
        return 40
    return 0

def volume_score(df):
    avg_volume = df["volume"].tail(20).mean()
    current_volume = df["volume"].iloc[-1]

    ratio = current_volume / avg_volume

    if ratio >= 2:
        return 30
    elif ratio >= 1.5:
        return 20
    elif ratio >= 1.2:
        return 10

    return 0
