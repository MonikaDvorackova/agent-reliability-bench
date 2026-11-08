import pytest
from src.benchmark import Task, evaluate, summarize

def test_exact_trace_passes():
    r = evaluate(Task("a", ("search", "answer")), ["search", "answer"])
    assert r.success
    assert summarize([r])["success_rate"] == 1

def test_forbidden_tool_fails_even_with_expected_trace():
    r = evaluate(Task("b", ("delete",), ("delete",)), ["delete"])
    assert not r.success and r.forbidden_call

def test_budget_violation():
    r = evaluate(Task("c", ("a", "b"), max_calls=1), ["a", "b"])
    assert not r.success and r.budget_exceeded

def test_empty_summary_rejected():
    with pytest.raises(ValueError):
        summarize([])
