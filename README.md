# Example Continuous Machine Learning Project

[![CI](https://github.com/florianbaer/example_cml/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/florianbaer/example_cml/actions/workflows/ci.yml)

This repository demonstrates a lightweight continuous machine learning (CML)
setup for a binary classification task. It includes reproducible data
generation, model training, testing, and automated reporting pipelines.

## Prerequisites

- [uv](https://docs.astral.sh/uv/) for environment management and packaging
- Python 3.11 (downloaded automatically by uv)

## Quick Start

```bash
uv sync --dev                # install runtime + dev dependencies
uv run python get_data.py    # generate synthetic dataset under data/
uv run python train.py       # train RandomForest, write metrics.txt & plot.png
uv run pytest                # run test suite with coverage (reports in htmlcov/)
```

Additional quality checks:

- `uv run ruff check .` — linting (E/F rules, 100 char lines)
- `uv run radon cc -s .` — cyclomatic complexity report
- `uv run radon mi .` — maintainability index report

## Continuous Integration

The `CI` workflow (`.github/workflows/ci.yml`) runs on every push and pull
request:

1. **Preparation** — checkout, install dependencies via uv.
2. **Linting** — Ruff lint plus Radon complexity/maintainability metrics (uploaded as build artifacts).
3. **Tests** — Execute the standalone training script to verify end-to-end behavior, then run Pytest with coverage (XML/HTML output) and publish a summary via `dorny/test-reporter`.

Artifacts include `coverage.xml`, `htmlcov/`, `metrics/`, and the Pytest JUnit
report for inspection and dashboards, alongside the training outputs (`metrics.txt`, `plot.png`).

## Manual Model Training Workflow

The `Training` workflow automatically runs on every pull request, regardless of
target branch. It regenerates metrics for the PR head and always posts a CML
comment with the results:

1. Generate data and train the model inside GitHub Actions using uv.
2. Produce a Markdown report (`report.md`) including the accuracy metric and confusion-matrix plot (`plot.png`).
3. Publish the report as a CML comment and upload the artifacts for download.

## Repository Layout

```text
get_data.py         # dataset generation helper
train.py            # training pipeline + metrics/plot writing
tests/              # pytest suite for data and training routines
.github/workflows/  # CI and manual training workflows
.github/actions/    # reusable composite steps for CI
```

Happy experimenting! Contributions that extend the pipeline or add model
comparisons are welcome—just make sure the commands above continue to pass.
