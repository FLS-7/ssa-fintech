import sqlite3
from pathlib import Path
import pandas as pd

DB_PATH = Path("data") / "ssa.db"
SQL_PATH = Path("sql") / "silver_anomalies.sql"
OUT_CSV = Path("data") / "silver_processed.csv"

def run_sql() -> None:
    if not DB_PATH.exists():
        return
    sql = SQL_PATH.read_text(encoding="utf-8")
    conn = sqlite3.connect(DB_PATH)
    conn.executescript(sql)
    df = pd.read_sql_query("SELECT * FROM silver_alerts", conn)
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT_CSV, index=False)
    conn.close()

def main() -> None:
    run_sql()

if __name__ == "__main__":
    main()
