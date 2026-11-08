from pathlib import Path

def test_static_space_files_exist():
    root = Path(__file__).resolve().parents[1] / "static-space"
    html = (root / "index.html").read_text(encoding="utf-8")
    metadata = (root / "README.md").read_text(encoding="utf-8")
    assert "sdk: static" in metadata
    assert 'id="form"' in html
    assert 'id="result"' in html
    assert "fetch(" not in html
    assert "forbidden_calls" in html
