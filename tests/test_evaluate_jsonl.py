import json
import pytest
from scripts.evaluate_jsonl import evaluate_jsonl

def test_batch(tmp_path):
    source = tmp_path / "traces.jsonl"
    source.write_text(
        '{"task_id":"a","expected_tools":["search"],"observed_tools":["search"]}\n'
        '{"task_id":"b","expected_tools":["search"],"observed_tools":["delete"],"forbidden_tools":["delete"]}\n'
    )
    target = tmp_path / "report.json"
    report = evaluate_jsonl(str(source), str(target))
    assert report["metrics"]["success_rate"] == 0.5
    assert report["metrics"]["forbidden_call_rate"] == 0.5
    assert json.loads(target.read_text()) == report

@pytest.mark.parametrize("line", [
    '{"task_id":"a","expected_tools":[],"observed_tools":[],"max_calls":true}',
    '{"task_id":"a","expected_tools":["x"],"observed_tools":"x"}',
    '{"task_id":"a","expected_tools":[]}',
    'not json',
])
def test_invalid_row(tmp_path, line):
    source = tmp_path / "bad.jsonl"
    source.write_text(line + "\n")
    with pytest.raises(ValueError, match="row 1"):
        evaluate_jsonl(str(source), str(tmp_path / "out.json"))
