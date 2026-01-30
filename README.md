#  SentinelPay — AI-Powered Fraud Detection Platform

SentinelPay is an **end-to-end FinTech fraud detection system** that demonstrates how machine learning models are integrated into real-world applications using backend APIs, user-facing dashboards, and compliance-aware system design.

The project focuses on **explainability, scalability, and production-style architecture**, not just model accuracy.

---

##  Key Highlights

- 🔍 Machine Learning–driven fraud detection  
- 🧠 Explainable AI (SHAP) for model transparency  
- ⚙️ FastAPI backend for real-time inference  
- 🎨 Streamlit frontend for interactive risk assessment  
- 🔐 Blockchain audit layer (design intent) for compliance  
- 🏗️ Clean, modular project architecture  

---

##  Problem Statement

Financial fraud detection systems must:
- Identify suspicious transactions accurately
- Operate in real time
- Be interpretable for audits and regulators
- Integrate cleanly with production systems

SentinelPay addresses these requirements by combining:
- ML-based fraud modeling
- API-driven deployment
- User-friendly interfaces
- Immutable audit trail design

---

##  System Architecture

User / Transaction
↓
Frontend Dashboard (Streamlit)
↓
Backend API (FastAPI)
↓
Fraud Detection Logic (ML / Heuristic)
↓
Risk Score + Decision
↓
Blockchain Audit Layer (Design)


---

## Project Structure

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
│   └── README.md           # Blockchain audit design
│
├── data/
│   └── creditcard.csv
│
└── README.md               # Project overview


## Machine Learning Overview

### Dataset
- Credit card transaction dataset with severe class imbalance
- Fraud cases represent a very small minority of total transactions

### Techniques Used
- Exploratory Data Analysis (EDA)
- Feature scaling and feature engineering
- SMOTE for handling class imbalance
- Random Forest classifier
- Isolation Forest for anomaly detection
- Precision–Recall based evaluation metrics

### Explainability
- Feature importance analysis
- SHAP (SHapley Additive exPlanations)
- Strong focus on regulatory transparency and interpretability

---

## Fraud Signals Used in the Application

The frontend accepts **human-readable transaction attributes**, rather than raw numerical feature vectors.

| Input | Description |
|------|------------|
| Transaction Amount | Monetary value of the transaction |
| Time Since Last Transaction | Behavioral timing signal |
| Transactions in Last Hour | Velocity / burst detection |
| Merchant Risk Score | Historical merchant risk score (0–1) |

These inputs are **translated in the backend** into model-ready features, mirroring how real-world production fraud systems operate.

---

## Backend API (FastAPI)

### Endpoints
- `GET /` — Health check endpoint  
- `POST /predict` — Fraud risk prediction endpoint  

### Example Request
```json
{
  "amount": 4500,
  "time_since_last_txn": 120,
  "txn_count_1hr": 6,
  "merchant_risk": 0.8
}

