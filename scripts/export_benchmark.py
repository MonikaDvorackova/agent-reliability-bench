"""Export a reproducible benchmark JSON artifact; no external services required."""
import json
from pathlib import Path
from experiments.reliability_suite import run

def export(destination: str = "artifacts/benchmark.json") -> Path:
    target = Path(destination)
    target.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "schema_version": "1.0",
        "benchmark": "agent-reliability-bench",
        "methodology": "deterministic exact tool-trace compliance",
        "limitations": "Fixture results only; not model quality or real-agent evaluation.",
        **run(),
    }
    target.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return target

if __name__ == "__main__":
    print(export())
