# 🚀 SSA-Fintech Intelligence Pipeline

![Python](https://img.shields.io/badge/python-3.11+-blue.svg?style=for-the-badge&logo=python)
![SQL](https://img.shields.io/badge/SQL-Advanced-orange.svg?style=for-the-badge&logo=postgresql)
![Architecture](https://img.shields.io/badge/Architecture-Medallion-green.svg?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-In%20Progress-orange?style=for-the-badge)

<p align="center">
  <b>Leia em Português:</b> <a href="README-PT.md">🇧🇷 Português</a>
</p>

A high-performance data engineering pipeline designed for real-time credit risk assessment and anomaly detection, specifically calibrated for the metropolitan region of **Salvador, BA, Brazil**.

## 📌 Project Overview

This project simulates a fintech's data infrastructure, handling transaction ingestion, risk scoring, and automated reporting. It utilizes the **Medallion Architecture** to ensure data quality and scalability, moving from raw events to executive-ready business insights.

## 🏗️ Data Architecture (Medallion Pattern)

1. **Bronze Layer (Raw):** Asynchronous ingestion of transaction data using `Python Asyncio` and `Faker`.
2. **Silver Layer (Trusted):** Data cleaning and complex transformations using `SQL Window Functions` (LAG/LEAD) to detect location hopping and suspicious patterns.
3. **Gold Layer (Business):** Final business logic and risk scoring, exported to a CSV of anomalies (`gold_anomalies.csv`) consumed by dashboards (e.g., Google Sheets + Looker Studio).

## 🛠️ Tech Stack

* **Language:** Python 3.11+ (focus on `asyncio`, `pandas`, `pytest`)
* **Database:** SQLite (Relational Storage)
* **Analytics:** SQL (Window Functions, CTEs)
* **Automation:** Python pipelines exporting BI-ready CSVs (no mandatory cloud API dependency in the core flow).
* **Visualization:** Looker Studio (Executive Dashboard) via Google Sheets or any dashboard tool connected to the Gold CSV.

## 📈 Key Engineering Features

* **Real-Time Simulation:** Asynchronous generation of 1,000+ concurrent transactions.
* **Anomaly Detection:** SQL-based logic to identify high-risk operations between distant neighborhoods in short timeframes.
* **Automated Pipeline:** Full ETL process from raw CSV to cloud-based BI dashboards.

## 🗺️ Roadmap (Upcoming Commits)

* [x] Initial architecture and documentation
* [x] Asynchronous data ingestion engine (Bronze)
* [x] SQL transformation and risk logic (Silver)
* [x] API integration and automation (Gold)
* [x] Final dashboard and unit testing (QA)

## ▶️ How to run the pipeline

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the full pipeline:
   ```bash
   python -m src.pipeline
   ```
3. Generated artifacts:
   - DB: `data/ssa.db` (`bronze_transactions` table)
   - Silver: `data/silver_processed.csv` (includes `anomaly_flag`)
   - Gold: `data/gold_anomalies.csv` (only non-`Normal` flags)

## 📊 Dashboard guide (Looker Studio via Google Sheets)

* Import `data/gold_anomalies.csv` into a Google Sheet.
* In Looker Studio, create a data source connected to that sheet.
* Suggested visuals:
  * Time series of anomaly counts by hour/day.
  * Bar chart by `neighborhood` split by anomaly flags.
  * Table of top transactions by `amount` with critical flags.

## ✅ Tests

* Run:
  ```bash
  pytest
  ```
* Coverage:
  * Ensures `bronze_transactions` exists with records.
  * Produces `silver_processed.csv` with `anomaly_flag`.
  * Produces `gold_anomalies.csv` as a filtered subset.
