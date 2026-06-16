def calculate_score(
    trend,
    volume,
    relative_strength,
    liquidity,
    momentum
):

    score = (
        trend * 0.30 +
        volume * 0.20 +
        relative_strength * 0.20 +
        liquidity * 0.15 +
        momentum * 0.15
    )

    return round(score)


def confidence(score):

    if score >= 85:
        return "A+"

    if score >= 75:
        return "A"

    if score >= 65:
        return "B"

    if score >= 55:
        return "C"

    return "D"
