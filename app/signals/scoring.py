def final_score(
    trend,
    structure,
    volume,
    oi,
    funding,
    liquidity
):
    return round(
        trend * 0.25 +
        structure * 0.25 +
        volume * 0.15 +
        oi * 0.15 +
        funding * 0.10 +
        liquidity * 0.10
    )
