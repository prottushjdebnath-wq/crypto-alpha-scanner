class RiskEngine:
    def __init__(self, equity=700):
        self.equity = equity

    def risk_amount(self):
        return round(self.equity * 0.005, 2)

    def daily_limit(self):
        return round(self.equity * 0.02, 2)

    def weekly_limit(self):
        return round(self.equity * 0.05, 2)
