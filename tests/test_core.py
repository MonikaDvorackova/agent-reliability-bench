from src.core import violation_rate

def test_rate():
    assert violation_rate([True, False, True]) == 1 / 3
