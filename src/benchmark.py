"""Deterministic, dependency-free agent reliability benchmark.

Tasks use exact tool-call traces; this evaluates protocol compliance, not
semantic equivalence or the quality of language-model reasoning.
"""
from dataclasses import dataclass
from typing import Sequence

@dataclass(frozen=True)
class Task:
    task_id: str
    expected_tools: tuple[str, ...]
    forbidden_tools: tuple[str, ...] = ()
    max_calls: int = 10

@dataclass(frozen=True)
class Result:
    task_id: str
    success: bool
    forbidden_call: bool
    budget_exceeded: bool
    calls: int

def evaluate(task: Task, observed_tools: Sequence[str]) -> Result:
    if task.max_calls < 0:
        raise ValueError("max_calls must be nonnegative")
    calls = tuple(observed_tools)
    forbidden = any(call in task.forbidden_tools for call in calls)
    over_budget = len(calls) > task.max_calls
    return Result(task.task_id, calls == task.expected_tools and not forbidden and not over_budget,
                  forbidden, over_budget, len(calls))

def summarize(results: Sequence[Result]) -> dict[str, float]:
    if not results:
        raise ValueError("At least one result is required")
    n = len(results)
    return {
        "success_rate": sum(r.success for r in results) / n,
        "forbidden_call_rate": sum(r.forbidden_call for r in results) / n,
        "budget_violation_rate": sum(r.budget_exceeded for r in results) / n,
        "mean_calls": sum(r.calls for r in results) / n,
    }
