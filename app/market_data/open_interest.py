def oi_score(current_oi, previous_oi):
    if previous_oi <= 0:
        return 0
    change = ((current_oi - previous_oi) / previous_oi) * 100
    if change >= 15:
        return 100
    if change >= 10:
        return 80
    if change >= 5:
        return 60
    return 20
