# GitHub Copilot Instructions

## General Guidance
- Prefer `uv` for environment setup, dependency installation, linting, tests, and coverage. Flag regressions to `pip install` or ad-hoc virtualenvs.
- Reuse `generate_data` and `train_model` helpers instead of duplicating CSV loading or model logic.
- Keep new tests under `tests/` and ensure they run with `pytest`; confirm coverage configuration in `pyproject.toml` stays effective.
- Verify CI workflow (`.github/workflows/ci.yml`) still produces Ruff, Radon, and pytest results, including artifacts and the test-reporter summary.
- Protect the manual `Training` workflow: it must continue to generate `metrics.txt`, `plot.png`, and (optionally) the CML comment.

## Pull Request Reviews
- Check for lint issues against Ruff's E/F rules and 100-character line limit; highlight unused imports or obvious style glitches.
- Ensure documentation (especially `README.md`) reflects any new commands, workflows, or artifacts.
- Validate workflow changes keep permissions minimal yet sufficient and still upload required artifacts (`coverage.xml`, `htmlcov/`, metrics, reports).
- Suggest additional regression tests when functionality expands or bugs are fixed.
- Note missing dependency updates in `pyproject.toml` whenever new libraries or tools appear in code or workflows.
