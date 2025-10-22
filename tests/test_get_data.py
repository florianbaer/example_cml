from pathlib import Path

import numpy as np

from get_data import generate_data


def test_generate_data_creates_expected_files(tmp_path: Path):
    outputs = generate_data(data_dir=tmp_path, seed=123, n_samples=200)

    expected_files = {
        "train_features.csv",
        "test_features.csv",
        "train_labels.csv",
        "test_labels.csv",
    }

    for filename in expected_files:
        assert (tmp_path / filename).exists(), f"Missing expected file: {filename}"

    loaded_train = np.loadtxt(tmp_path / "train_features.csv")
    loaded_test = np.loadtxt(tmp_path / "test_features.csv")
    loaded_train_labels = np.loadtxt(tmp_path / "train_labels.csv")
    loaded_test_labels = np.loadtxt(tmp_path / "test_labels.csv")

    assert loaded_train.shape == outputs["X_train"].shape
    assert loaded_test.shape == outputs["X_test"].shape
    assert loaded_train_labels.shape == outputs["y_train"].shape
    assert loaded_test_labels.shape == outputs["y_test"].shape

    assert np.allclose(loaded_train, outputs["X_train"])
    assert np.allclose(loaded_test, outputs["X_test"])
    assert np.allclose(loaded_train_labels, outputs["y_train"])
    assert np.allclose(loaded_test_labels, outputs["y_test"])
