def violation_rate(outcomes: list[bool]) -> float:
    """Fraction of tool-call traces violating a predefined rule."""
    if not outcomes:
        raise ValueError("Provide at least one outcome")
    return sum(not ok for ok in outcomes) / len(outcomes)
