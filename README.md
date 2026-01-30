# SentinelPay – AI-Powered Fraud Detection Platform

SentinelPay is an end-to-end FinTech fraud detection system that demonstrates how machine learning models are integrated into real-world applications using backend APIs, interactive dashboards, and compliance-aware system design.

The project focuses on **explainability, scalability, and production-style architecture** rather than model accuracy alone.

---

##  What does it do?

SentinelPay helps assess whether a financial transaction is fraudulent by analyzing behavioral and contextual signals.

**You provide:**
* **Transaction details:** Amount, timing, frequency, and merchant risk.

**The system returns:**
* **Fraud probability score:** A numerical likelihood of fraud.
* **Risk classification:** Categorized as `Low`, `Medium`, or `High`.

The platform demonstrates how ML models are deployed, consumed, and explained in modern financial ecosystems.

---

##  System Overview

The flow of data through the platform follows a modular, decoupled architecture:

1.  **User / Transaction:** Input via the interface.
2.  **Frontend Dashboard:** Built with **Streamlit** for real-time interaction.
3.  **Backend API:** **FastAPI** handles requests and serves as the bridge to the model.
4.  **Fraud Detection Logic:** Processing engine using Scikit-Learn.
5.  **Risk Score & Decision:** Output returned to the user.
6.  **Blockchain Audit Layer:** Proposed immutable logging for compliance.



---

##  Project Structure

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
│   └── creditcard.csv      # Source dataset (Kaggle/Synthetic)
│
└── README.md               # Main project documentation

```
