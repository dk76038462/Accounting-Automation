# Accounting Transaction Automation & Financial Dashboard

This repository contains a small accounting automation pipeline that:
1. Reads transaction data from a CSV file  
2. Generates summary reports using Python and pandas  
3. Visualises the results as simple financial dashboards using matplotlib  

The goal is to show how basic automation can reduce manual workload in bookkeeping and support data-driven decision making.

---

## 📌 Project Overview

The project is split into two main parts:

1. **Automation & Summaries**  
   - Load raw transaction data from `data/sample_transactions.csv`  
   - Generate summary reports by:
     - **type** (Income / Expense)
     - **account_code**
     - **date** (daily net income)
   - Save the results into the `output/` folder as CSV files

2. **Financial Dashboard**  
   - Read the summary CSV files from `output/`  
   - Create simple charts using matplotlib  
   - Export the charts as PNG images into the `images/` folder

This mini pipeline connects basic accounting knowledge with Python, pandas, and simple visualisation.

---

## 📂 Folder Structure

```text
Accounting-Automation/
├── data/
│   └── sample_transactions.csv
│
├── output/
│   ├── summary_by_type.csv
│   ├── summary_by_account.csv
│   └── daily_summary.csv
│
├── images/
│   ├── daily_net_income.png
│   ├── total_by_type.png
│   └── total_by_account.png
│
└── src/
    ├── main.py        # summary generator
    └── dashboard.py   # chart generator
