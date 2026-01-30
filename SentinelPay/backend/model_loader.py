import numpy as np

class FraudModel:
    """
    Converts human-readable transaction inputs into
    model-ready features and returns a fraud risk.
    """

    def __init__(self):
        self.threshold_low = 0.3
        self.threshold_high = 0.7

    def predict(self, data):
        # Simple, realistic feature engineering
        features = np.array([
            data.amount / 10000.0,                     # normalize amount
            min(data.time_since_last_txn / 3600.0, 1), # cap at 1 hour
            min(data.txn_count_1hr / 10.0, 1),         # activity intensity
            data.merchant_risk                         # already 0–1
        ])

        probability = float(np.clip(features.mean(), 0.01, 0.99))

        if probability < self.threshold_low:
            risk = "Low"
        elif probability < self.threshold_high:
            risk = "Medium"
        else:
            risk = "High"

        return probability, risk
