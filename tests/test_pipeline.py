from pathlib import Path
import sqlite3
import pandas as pd

from src.pipeline import run
from src.silver_exec import run_sql
from src.gold_orchestrator import build_gold_layer

def test_bronze_table_exists():
    run()
    db_path = Path("data") / "ssa.db"
    conn = sqlite3.connect(db_path)
    cur = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='bronze_transactions'")
    rows = cur.fetchall()
    assert rows, "bronze_transactions missing"
    count = conn.execute("SELECT COUNT(*) FROM bronze_transactions").fetchone()[0]
    assert count > 0
    conn.close()

def test_silver_processed_csv_exists():
    run_sql()
    csv_path = Path("data") / "silver_processed.csv"
    assert csv_path.exists()
    df = pd.read_csv(csv_path)
    assert "anomaly_flag" in df.columns

def test_gold_has_anomalies_file():
    build_gold_layer()
    gold_path = Path("data") / "gold_anomalies.csv"
    assert gold_path.exists()
    df = pd.read_csv(gold_path)
    assert "anomaly_flag" in df.columns
