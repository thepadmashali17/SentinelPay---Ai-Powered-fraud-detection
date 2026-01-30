from pydantic import BaseModel

class TransactionInput(BaseModel):
    amount: float
    time_since_last_txn: float
    txn_count_1hr: int
    merchant_risk: float


class PredictionResponse(BaseModel):
    fraud_probability: float
    risk_level: str
