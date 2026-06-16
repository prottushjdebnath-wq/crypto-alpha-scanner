from app.market_data.open_interest import oi_score
from app.market_data.funding import funding_score
from app.market_data.liquidity import liquidity_score
from app.signals.scoring import final_score

coins = [
    {
        "symbol": "BTCUSDT",
        "trend": 100,
        "structure": 100,
        "volume": 80,
        "oi_now": 115,
        "oi_prev": 100,
        "funding": 0.005,
        "volume_24h": 100000000
    },
    {
        "symbol": "ETHUSDT",
        "trend": 100,
        "structure": 80,
        "volume": 80,
        "oi_now": 108,
        "oi_prev": 100,
        "funding": 0.012,
        "volume_24h": 70000000
    }
]

for c in coins:

    oi = oi_score(c["oi_now"], c["oi_prev"])
    funding = funding_score(c["funding"])
    liquidity = liquidity_score(c["volume_24h"])

    score = final_score(
        c["trend"],
        c["structure"],
        c["volume"],
        oi,
        funding,
        liquidity
    )

    print(
        f"{c['symbol']} | "
        f"Score={score} | "
        f"OI={oi} | "
        f"Funding={funding} | "
        f"Liquidity={liquidity}"
    )
