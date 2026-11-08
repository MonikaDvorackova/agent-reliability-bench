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

## Try it and share results

- Export a deterministic benchmark artifact: `python -m scripts.export_benchmark`.
- GitHub Actions automatically validates and uploads `benchmark-results` on every PR and push to main.
- A standalone Gradio demo is in [space/](space/). Run locally with `pip install -r space/requirements.txt && python space/app.py`.
- Optional Hugging Face dataset + Space publication is **manual and credential-gated**. See [distribution setup](docs/DISTRIBUTION.md).
- Report bugs and reproducible trace failures through [GitHub Issues](https://github.com/MonikaDvorackova/agent-reliability-bench/issues).

No social posts, Hugging Face uploads, or third-party account changes are performed without explicit configuration.

## Batch evaluation of tool traces

Run `python -m scripts.evaluate_jsonl examples/agent_traces.jsonl -o artifacts/batch-results.json`.

Each JSONL record requires `task_id` (string), `expected_tools` (list of strings), and `observed_tools` (list of strings). Optional fields: `forbidden_tools` (list of strings) and `max_calls` (nonnegative integer, default 10). Output includes per-case results and aggregate success, forbidden-call, budget-violation, and mean-call metrics. Inputs are evaluated locally; no third-party model is contacted. See [public demo](https://monikadvorackova.github.io/agent-reliability-bench/).

## Run without local setup

Use [CI](https://github.com/MonikaDvorackova/agent-reliability-bench/actions/workflows/ci.yml) → Run workflow to validate remotely, or [Benchmark artifact](https://github.com/MonikaDvorackova/agent-reliability-bench/actions/workflows/benchmark-artifact.yml) → Run workflow to generate a downloadable benchmark JSON. For custom JSONL, clone the repository and execute from its root, not your home directory.

## Project showcase and feedback

Part of a public [trustworthy AI and reliable ML research engineering portfolio](https://github.com/MonikaDvorackova/MonikaDvorackova#research-engineering-projects). For project scope, test coverage and limitations, see this README and the repository's GitHub Actions. Reproducible issues and narrowly scoped contributions are welcome. These reference implementations are not certified production systems.
