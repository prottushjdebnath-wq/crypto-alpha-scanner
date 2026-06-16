def liquidity_score(volume_24h):
    if volume_24h >= 50000000:
        return 100
    if volume_24h >= 20000000:
        return 80
    return 0
