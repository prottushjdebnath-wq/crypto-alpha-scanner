def funding_score(rate):
    if abs(rate) < 0.01:
        return 100
    if abs(rate) < 0.03:
        return 70
    return 30
