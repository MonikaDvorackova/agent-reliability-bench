"""Evaluate JSONL tool-call traces with the same exact-match semantics as the reference benchmark.

Each input line must contain task_id, expected_tools, observed_tools,
and optional forbidden_tools and max_calls. This is not semantic evaluation.
"""
import argparse
import json
from dataclasses import asdict
from pathlib import Path
from src.benchmark import Task, evaluate, summarize

def _tools(obj, key, required=False):
    value = obj.get(key)
    if value is None and not required:
        return ()
    if not isinstance(value, list) or any(not isinstance(x, str) for x in value):
        raise ValueError(f"{key} must be a list of strings")
    return tuple(value)

def evaluate_jsonl(source: str, destination: str) -> dict:
    rows = []
    for line_number, line in enumerate(Path(source).read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            obj = json.loads(line)
            if not isinstance(obj, dict):
                raise ValueError("row must be a JSON object")
            task_id = obj.get("task_id")
            if not isinstance(task_id, str) or not task_id:
                raise ValueError("task_id must be a nonempty string")
            max_calls = obj.get("max_calls", 10)
            if type(max_calls) is not int or max_calls < 0:
                raise ValueError("max_calls must be a nonnegative integer")
            task = Task(task_id, _tools(obj, "expected_tools", True),
                        _tools(obj, "forbidden_tools"), max_calls)
            result = evaluate(task, _tools(obj, "observed_tools", True))
            rows.append(result)
        except (ValueError, TypeError, json.JSONDecodeError) as exc:
            raise ValueError(f"Invalid JSONL row {line_number}: {exc}") from exc
    if not rows:
        raise ValueError("Input must contain at least one case")
    report = {
        "schema_version": "1.0",
        "methodology": "exact tool-name sequence matching",
        "metrics": summarize(rows),
        "cases": [asdict(row) for row in rows],
    }
    output = Path(destination)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return report

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Input JSONL file")
    parser.add_argument("-o", "--output", default="artifacts/batch-results.json")
    args = parser.parse_args()
    print(json.dumps(evaluate_jsonl(args.input, args.output)["metrics"], indent=2))
