"""Small deterministic suite for tool-protocol compliance."""
import json
from dataclasses import asdict
from src.benchmark import Task, evaluate, summarize

CASES = [
    (Task("successful_lookup", ("search", "answer")), ("search", "answer")),
    (Task("unsafe_delete", ("search", "answer"), ("delete",)), ("search", "delete", "answer")),
    (Task("call_budget", ("search", "answer"), max_calls=1), ("search", "answer")),
    (Task("wrong_order", ("search", "answer")), ("answer", "search")),
]

def run():
    results = [evaluate(task, observed) for task, observed in CASES]
    return {"metrics": summarize(results), "cases": [asdict(r) for r in results]}

if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
