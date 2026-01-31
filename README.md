# SentinelPay – AI-Powered Fraud Detection Platform

SentinelPay is an end-to-end **FinTech fraud detection platform** that demonstrates how machine learning models are integrated into real-world systems using backend APIs, interactive dashboards, and compliance-aware design.

Rather than focusing only on model accuracy, this project emphasizes:

- Explainability (XAI)
- Scalability
- Production-style system architecture
- Regulatory and compliance awareness

---

## 🚀 What Does SentinelPay Do?

SentinelPay assesses whether a financial transaction is potentially fraudulent by analyzing behavioral and contextual signals.

### 🔹 Input
Users provide transaction-related details such as:
- Transaction amount  
- Time since last transaction  
- Transaction frequency  
- Merchant risk score  

### 🔹 Output
The system returns:
- **Fraud Probability Score** – numerical likelihood of fraud  
- **Risk Classification** – `Low`, `Medium`, or `High`

This project simulates how fraud detection models are **deployed, consumed, and explained** in modern financial ecosystems.

---

## 🧩 System Architecture Overview

The platform follows a **modular and decoupled architecture**:

1. **User / Transaction Input**
2. **Frontend Dashboard** – Streamlit-based UI
3. **Backend API** – FastAPI service
4. **Fraud Detection Engine** – ML logic (Scikit-Learn)
5. **Risk Scoring & Decision**
6. **Blockchain Audit Layer (Design Proposal)** – Immutable compliance logs

---

## 📁 Project Structure

```text
SentinelPay/
├── backend/
│   ├── app.py              # FastAPI application
│   ├── schemas.py          # Request/response validation
│   ├── model_loader.py     # Fraud prediction logic
│   └── README.md
│
├── frontend/
│   └── app.py              # Streamlit dashboard
│
├── ml/
│   └── notebooks/
│       ├── 01_data_exploration.ipynb
│       ├── 02_feature_engineering.ipynb
│       ├── 03_model_training.ipynb
│       └── 04_model_explainability.ipynb
│
├── blockchain/
│   └── README.md           # Blockchain audit design documentation
│
├── data/
│   └── creditcard.csv      # Source dataset (Kaggle / Synthetic)
│
└── README.md               # Main project documentation
🤖 Machine Learning Overview
Dataset
Credit card transaction dataset with severe class imbalance

Fraudulent transactions form a very small minority

Techniques Used
Exploratory Data Analysis (EDA)

Feature scaling & feature engineering

SMOTE for handling class imbalance

Random Forest classifier

Isolation Forest for anomaly detection

Precision–Recall focused evaluation metrics

Explainability (XAI)
Feature importance analysis

SHAP (SHapley Additive exPlanations)

Designed with regulatory transparency in mind

🔌 Backend API (FastAPI)
Available Endpoints
GET / – Health check

POST /predict – Fraud risk prediction

Sample Request
{
  "amount": 4500,
  "time_since_last_txn": 120,
  "txn_count_1hr": 6,
  "merchant_risk": 0.8
}
📊 Frontend Dashboard (Streamlit)
The Streamlit dashboard allows users to:

Enter transaction details

Submit real-time prediction requests

View fraud probability and risk classification instantly

🔗 Blockchain Audit Layer (Design Intent)
To support compliance and trust, SentinelPay proposes a blockchain-based audit layer.

Purpose
Immutable fraud decision logs

Tamper-proof audit trails

Regulatory readiness

Key Design Principle
No raw transaction or personal data stored on-chain

Only hashed metadata and decision summaries are recorded

⚠️ This layer is documented but not deployed, reflecting realistic FinTech adoption practices.

⚙️ How to Run the Project Locally
Step 1: Activate Virtual Environment
.venv\Scripts\activate
Step 2: Start Backend API
uvicorn backend.app:app --reload
Open API Docs:

http://127.0.0.1:8000/docs
Step 3: Start Frontend Dashboard
streamlit run frontend/app.py
🛠 Tech Stack
Python

FastAPI

Streamlit

Scikit-learn

SHAP

Pandas

NumPy

🎯 Skills Demonstrated
Applied Machine Learning

Explainable AI (XAI)

Backend API Development

Frontend Integration

End-to-End System Design

FinTech Compliance Awareness

Production-Style Project Structuring

🔮 Future Enhancements
Replace heuristic logic with fully trained ML model in backend

Persist fraud decisions to a blockchain testnet

Add authentication and role-based access control

Containerize and deploy using Docker & cloud infrastructure
