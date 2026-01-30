# SentinelPay – Blockchain Audit Layer (Design Intent)

## Overview
In financial systems, fraud decisions must be **auditable, tamper-proof, and traceable**.
SentinelPay proposes a blockchain-based audit layer to ensure trust and compliance in fraud detection decisions.

This module outlines the **design intent** for integrating blockchain into the fraud detection pipeline.

---

## Why Blockchain?
Fraud detection systems operate in regulated environments where:
- Decisions may be disputed
- Models may be audited
- Logs must not be altered

Blockchain provides:
- Immutability
- Transparency
- Verifiable audit trails

---

## What Would Be Stored On-Chain
Only **metadata**, never raw customer data.

Example on-chain record:
```json
{
  "transaction_id": "txn_987654",
  "timestamp": "2026-01-31T10:45:00Z",
  "fraud_probability": 0.82,
  "risk_level": "High",
  "model_version": "v1.0",
  "decision_hash": "0xA94F..."
}
