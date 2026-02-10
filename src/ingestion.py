import csv
import math
import random
from pathlib import Path
from typing import Iterator, Tuple

from faker import Faker


faker = Faker("pt_BR")

# Lista enxuta de bairros de Salvador (mistura de zonas litorâneas e centrais)
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


def clamp(v: float, low: float, high: float) -> float:
    return max(low, min(high, v))


def renda_brl() -> float:
    # Distribuição lognormal para renda mensal (captura assimetria típica de renda)
    # mu/sigma calibrados para ~R$ 1.5k–20k, com cauda superior moderada
    val = random.lognormvariate(mu=7.5, sigma=0.6)
    return round(val, 2)


def score_serasa() -> int:
    # Score aproximado, centrado em 600 com dispersão moderada
    s = int(random.gauss(600, 120))
    return max(0, min(1000, s))


def gasto_mensal(renda: float, score: int) -> float:
    # Relação gasto/renda aumenta levemente com score; ruído controla variabilidade
    base_share = clamp(0.35 + (score - 500) / 1000 * 0.3, 0.25, 0.85)
    noise = random.uniform(-0.05, 0.08)
    share = clamp(base_share + noise, 0.2, 0.9)
    return round(renda * share, 2)


def gen_client() -> Tuple[str, str, float, int, float]:
    name = faker.name()
    neighborhood = random.choice(NEIGHBORHOODS)
    income = renda_brl()
    score = score_serasa()
    spend = gasto_mensal(income, score)
    return name, neighborhood, income, score, spend


def generate_rows(n: int) -> Iterator[Tuple[str, str, float, int, float]]:
    for _ in range(n):
        yield gen_client()


def write_csv(path: Path, rows: Iterator[Tuple[str, str, float, int, float]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Nome", "Bairro", "Renda", "ScoreSerasa", "GastoMensal"])
        for row in rows:
            writer.writerow(row)


def main() -> None:
    outfile = Path("data") / "clients.csv"
    write_csv(outfile, generate_rows(1000))
    print(f"CSV gerado: {outfile.resolve()}")


if __name__ == "__main__":
    main()

