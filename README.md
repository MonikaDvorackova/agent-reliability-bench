# agent-reliability-bench

Deterministic tool-trace protocol evaluation.

## Scope

A small, inspectable, reproducible **v0.1 reference implementation**. The project is not presented as a production system or peer-reviewed research result.

## Requirements

Python 3.12

## Setup

```bash
python -m pip install pytest
```

## Run example / experiment

From the repository root:

```bash
python -m experiments.reliability_suite
```

## Test

```bash
python -m pytest -q
```

## Reproducibility

Experiments use deterministic inputs or explicitly seeded generators. See the experiment sources for assumptions and input sizes. CI exercises both tests and the example; check the Actions tab for actual run results. No empirical results are claimed without executed measurements.

## Limitations

Exact tool-name sequences are compared; semantic equivalence, model reasoning quality, live agent integrations and statistical confidence intervals are out of scope.

## License

MIT. Contributions should include a focused regression test and an explanation of changed assumptions.
