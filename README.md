# Example Continuous Machine Learning project

This repository contains code and data for a simple classification problem. All
commands below assume you have [uv](https://docs.astral.sh/uv/) installed.

- `uv sync --dev` creates a virtual environment with runtime and test dependencies.
- `uv run python get_data.py` generates the dataset under the `data/` folder.
- `uv run python train.py` trains the classifier and stores the resulting metrics and plot.
- `uv run pytest` runs the automated test suite.
- `uv run ruff check .` performs linting to enforce code style and catch common errors.
- `uv run radon cc -s .` and `uv run radon mi .` report cyclomatic complexity and maintainability metrics.
- `uv run pytest --cov=.` can be used when you want to rerun tests with coverage summaries on demand (the default `uv run pytest` already produces coverage reports courtesy of `pyproject.toml`).

To generate a model performance report from GitHub Actions, launch the manual
`Training` workflow (`Actions > Training > Run workflow`). It trains the model,
collects metrics, and posts a CML report containing the confusion matrix plot.
