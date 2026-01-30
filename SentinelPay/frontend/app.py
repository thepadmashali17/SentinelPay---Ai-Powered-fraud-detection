import streamlit as st
import requests

st.set_page_config(page_title="SentinelPay Fraud Detector", layout="centered")

st.title("💳 SentinelPay – Fraud Detector")
st.write("Enter transaction details to assess fraud risk.")

with st.form("txn_form"):
    amount = st.number_input("Transaction Amount", min_value=0.0, step=10.0)
    time_since = st.number_input("Seconds Since Last Transaction", min_value=0.0, step=10.0)
    txn_count = st.number_input("Transactions in Last Hour", min_value=0, step=1)
    merchant_risk = st.slider("Merchant Risk Score (0–1)", 0.0, 1.0, 0.5)

    submitted = st.form_submit_button("Predict Fraud Risk")

if submitted:
    payload = {
        "amount": amount,
        "time_since_last_txn": time_since,
        "txn_count_1hr": int(txn_count),
        "merchant_risk": merchant_risk
    }

    try:
        resp = requests.post("http://127.0.0.1:8000/predict", json=payload, timeout=5)
        if resp.status_code == 200:
            res = resp.json()
            st.success("Prediction Successful")
            st.metric("Fraud Probability", f"{res['fraud_probability']:.2f}")
            st.metric("Risk Level", res["risk_level"])
        else:
            st.error("Backend error. Check API.")
    except Exception as e:
        st.error(f"Connection error: {e}")
