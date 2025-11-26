# Accounting Transaction Automation – Summary Generator

This project is a small accounting automation tool that reads transaction data from a CSV file and produces summary reports.  
It is designed to demonstrate how basic automation can reduce manual workload in bookkeeping and support data-driven decision making.

---

## 📌 Project Overview

The script:

- Loads transaction data from `data/sample_transactions.csv`
- Summarises totals by:
  - **type** (Income / Expense)
  - **account_code**
  - **date** (daily net income)
- Saves the results as CSV files in the `output/` folder

This project combines basic accounting knowledge with Python and pandas, and can be extended into dashboards or further analytics.

---

## 📂 Folder Structure

```text
Accounting-Automation/
├── data/
│   └── sample_transactions.csv
├── output/
│   ├── summary_by_type.csv
│   ├── summary_by_account.csv
│   └── daily_summary.csv
└── src/
    └── main.py
