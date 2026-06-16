import pandas as pd


def trend_score(df):

    ema50 = df["close"].ewm(span=50).mean()
    ema200 = df["close"].ewm(span=200).mean()

    return 100 if ema50.iloc[-1] > ema200.iloc[-1] else 20


def volume_score(df):

    avg_volume = df["volume"].tail(50).mean()
    current_volume = df["volume"].iloc[-1]

    if current_volume > avg_volume * 3:
        return 100

    if current_volume > avg_volume * 2:
        return 90

    if current_volume > avg_volume * 1.5:
        return 80

    return 40


def momentum_score(df):

    change = (
        df["close"].iloc[-1]
        -
        df["close"].iloc[-20]
    ) / df["close"].iloc[-20]

    if change > 0.10:
        return 100

    if change > 0.05:
        return 90

    if change > 0:
        return 70

    return 30


def liquidity_score(df):

    avg_dollar_volume = (
        df["close"] * df["volume"]
    ).tail(50).mean()

    if avg_dollar_volume > 50000000:
        return 100

    if avg_dollar_volume > 20000000:
        return 80

    return 30


def relative_strength_score(df):

    close = df["close"]

    if len(close) < 30:
        return 50

    rs = (
        close.iloc[-1]
        /
        close.iloc[-30]
    )

    if rs > 1.20:
        return 100

    if rs > 1.10:
        return 90

    if rs > 1.00:
        return 75

    return 40
