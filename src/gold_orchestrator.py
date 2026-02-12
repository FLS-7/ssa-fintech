from pathlib import Path
from typing import List

import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

SHEETS_SCOPE = ["https://www.googleapis.com/auth/spreadsheets"]
DEFAULT_SPREADSHEET_NAME = "SSA_Fintech_Gold"
DEFAULT_CREDS_PATH = "creds.json"
DEFAULT_CSV_PATH = "data/silver_processed.csv"


def _authorize(creds_path: str) -> gspread.Client:
    # Escopo mínimo necessário para Sheets API
    creds = ServiceAccountCredentials.from_json_keyfile_name(creds_path, SHEETS_SCOPE)
    return gspread.authorize(creds)


def push_to_gold_layer(
    csv_path: str = DEFAULT_CSV_PATH,
    spreadsheet_name: str = DEFAULT_SPREADSHEET_NAME,
    creds_path: str = DEFAULT_CREDS_PATH,
) -> None:
    csv_file = Path(csv_path)
    if not csv_file.exists():
        print(f"Arquivo não encontrado: {csv_file.resolve()}")
        return

    df = pd.read_csv(csv_file)

    # Regra de negócio: publica apenas registros com alguma anomalia
    gold_df = df[df.get("anomaly_flag", "Normal") != "Normal"]

    client = _authorize(creds_path)
    sheet = client.open(spreadsheet_name).sheet1

    payload: List[List[object]] = [gold_df.columns.tolist()] + gold_df.values.tolist()
    sheet.clear()
    sheet.update("A1", payload)
    print("Camada Gold atualizada no Google Sheets!")


if __name__ == "__main__":
    push_to_gold_layer()
