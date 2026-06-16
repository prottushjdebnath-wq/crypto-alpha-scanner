def calculate_score(
    trend_points,
    volume_points,
    relative_strength_points
):
    return (
        trend_points +
        volume_points +
        relative_strength_points
    )
