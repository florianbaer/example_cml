from pathlib import Path

import pytest

from get_data import generate_data
from train import train_model


def test_train_model_produces_metrics_and_plot(tmp_path: Path):
    generate_data(data_dir=tmp_path, seed=123, n_samples=200)

    metrics_path = tmp_path / "artifacts" / "metrics.txt"
    plot_path = tmp_path / "artifacts" / "plot.png"

    results = train_model(
        data_dir=tmp_path,
        max_depth=2,
        random_state=0,
        metrics_path=metrics_path,
        plot_path=plot_path,
    )

    assert "accuracy" in results
    assert 0.0 <= results["accuracy"] <= 1.0
    assert results["accuracy"] > 0.5

    assert metrics_path.exists()
    metrics_text = metrics_path.read_text(encoding="utf-8").strip()
    assert metrics_text.startswith("Accuracy:")
    recorded_accuracy = float(metrics_text.split(":", maxsplit=1)[1])
    assert results["accuracy"] == pytest.approx(recorded_accuracy, rel=1e-6)

    assert plot_path.exists()
    assert plot_path.stat().st_size > 0
