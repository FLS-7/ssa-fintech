import asyncio
import random
import sqlite3
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Tuple
from faker import Faker

DB_PATH = Path("data") / "ssa.db"
TABLE_SQL = """
CREATE TABLE IF NOT EXISTS bronze_transactions (
  client_id TEXT,
  neighborhood TEXT,
  timestamp TEXT,
  amount REAL
);
"""
NEIGHBORHOODS = [
    "Barra",
    "Ondina",
    "Pituba",
    "Rio Vermelho",
    "Graça",
    "Itapuã",
    "Brotas",
    "Stiep",
    "Imbuí",
    "Piatã",
    "Caminho das Árvores",
    "Amaralina",
    "Boca do Rio",
    "Cabula",
    "Pernambués",
    "Federação",
    "Centro Histórico",
    "Nazaré",
    "Canela",
    "Costa Azul",
]
faker = Faker("pt_BR")

def gen_amount() -> float:
    return round(random.uniform(10, 10000), 2)

def gen_client_id() -> str:
    return faker.uuid4()

async def gen_transactions(client_id: str, n: int) -> List[Tuple[str, str, str, float]]:
    base_time = datetime.now()
    rows = []
    cur_neigh = random.choice(NEIGHBORHOODS)
    for i in range(n):
        hop = random.random() < 0.2
        if hop:
            cur_neigh = random.choice(NEIGHBORHOODS)
        delta = timedelta(seconds=random.randint(30, 1800))
        ts = base_time + delta * i
        rows.append((client_id, cur_neigh, ts.isoformat(), gen_amount()))
    await asyncio.sleep(0)
    return rows

def init_db() -> sqlite3.Connection:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.execute(TABLE_SQL)
    return conn

def insert_rows(conn: sqlite3.Connection, rows: List[Tuple[str, str, str, float]]) -> None:
    conn.executemany(
        "INSERT INTO bronze_transactions (client_id, neighborhood, timestamp, amount) VALUES (?, ?, ?, ?)",
        rows,
    )
    conn.commit()

async def run_ingestion(num_clients: int = 500, min_tx: int = 5, max_tx: int = 20) -> None:
    conn = init_db()
    tasks = []
    for _ in range(num_clients):
        cid = gen_client_id()
        n = random.randint(min_tx, max_tx)
        tasks.append(gen_transactions(cid, n))
    all_rows = await asyncio.gather(*tasks)
    flat_rows = [r for batch in all_rows for r in batch]
    insert_rows(conn, flat_rows)
    conn.close()

def main() -> None:
    asyncio.run(run_ingestion())

if __name__ == "__main__":
    main()
