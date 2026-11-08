import json
from scripts.export_benchmark import export

def test_export_is_reproducible(tmp_path):
    target = tmp_path / "result.json"
    export(str(target))
    first = target.read_bytes()
    export(str(target))
    assert target.read_bytes() == first
    result = json.loads(first)
    assert result["schema_version"] == "1.0"
    assert len(result["cases"]) == 4
    assert 0 <= result["metrics"]["success_rate"] <= 1
