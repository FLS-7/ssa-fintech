from pathlib import Path

import pandas as pd

DEFAULT_SILVER_CSV_PATH = "data/silver_processed.csv"
DEFAULT_GOLD_CSV_PATH = "data/gold_anomalies.csv"


def build_gold_layer(
    silver_csv_path: str = DEFAULT_SILVER_CSV_PATH,
    gold_csv_path: str = DEFAULT_GOLD_CSV_PATH,
) -> None:
    silver_file = Path(silver_csv_path)
    if not silver_file.exists():
        print(f"Arquivo não encontrado: {silver_file.resolve()}")
        return

    df = pd.read_csv(silver_file)

    gold_df = df[df.get("anomaly_flag", "Normal") != "Normal"]

    gold_path = Path(gold_csv_path)
    gold_path.parent.mkdir(parents=True, exist_ok=True)

    gold_df.to_csv(gold_path, index=False)
    print(f"Camada Gold exportada para CSV em: {gold_path.resolve()}")


if __name__ == "__main__":
    build_gold_layer()
