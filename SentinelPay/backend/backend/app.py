from fastapi import FastAPI
from backend.schemas import TransactionInput, PredictionResponse
from backend.model_loader import FraudModel

app = FastAPI(
    title="SentinelPay Fraud Detection API",
    description="API for predicting fraudulent financial transactions",
    version="1.0"
)

model = FraudModel()

@app.get("/")
def health_check():
    return {"status": "SentinelPay backend running"}

@app.post("/predict", response_model=PredictionResponse)
def predict_fraud(data: TransactionInput):
    probability, risk = model.predict(data)
    return PredictionResponse(
        fraud_probability=round(probability, 4),
        risk_level=risk
    )
