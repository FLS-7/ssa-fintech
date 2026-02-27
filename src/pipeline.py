from .bronze_async import main as bronze_main
from .silver_exec import main as silver_main
from .gold_orchestrator import build_gold_layer

def run() -> None:
    bronze_main()
    silver_main()
    build_gold_layer()

if __name__ == "__main__":
    run()
