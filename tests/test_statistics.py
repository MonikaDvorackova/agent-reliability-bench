import pytest
from src.statistics import wilson_interval

def test_wilson_bounds():
    lo,hi=wilson_interval(5,10)
    assert 0 < lo < 0.5 < hi < 1
    assert wilson_interval(0,10)[0]==0
    assert wilson_interval(10,10)[1]==1
    with pytest.raises(ValueError):
        wilson_interval(3,2)
