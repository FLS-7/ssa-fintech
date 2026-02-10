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
3. **Gold Layer (Business):** Final business logic and risk scoring, delivered via `Google Sheets API` to stakeholders.

## 🛠️ Tech Stack

* **Language:** Python 3.11+ (focus on `asyncio`, `pandas`, `pytest`)
* **Database:** SQLite (Relational Storage)
* **Analytics:** SQL (Window Functions, CTEs)
* **Automation:** Google Sheets API (`gspread`)
* **Visualization:** Looker Studio (Executive Dashboard)

## 📈 Key Engineering Features

* **Real-Time Simulation:** Asynchronous generation of 1,000+ concurrent transactions.
* **Anomaly Detection:** SQL-based logic to identify high-risk operations between distant neighborhoods in short timeframes.
* **Automated Pipeline:** Full ETL process from raw CSV to cloud-based BI dashboards.

## 🗺️ Roadmap (Upcoming Commits)

* [x] Initial architecture and documentation
* [x] Asynchronous data ingestion engine (Bronze)
* [ ] SQL transformation and risk logic (Silver)
* [ ] API integration and automation (Gold)
* [ ] Final dashboard and unit testing (QA)
