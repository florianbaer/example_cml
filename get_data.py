from pathlib import Path

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
import numpy as np


def generate_data(
    data_dir: str | Path = "data",
    seed: int = 42,
    n_samples: int = 1000,
):
    """Generate a synthetic binary classification dataset and store it on disk."""

    data_path = Path(data_dir)
    data_path.mkdir(parents=True, exist_ok=True)

    X, y = make_classification(n_samples=n_samples, random_state=seed)
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=seed)

    np.savetxt(data_path / "train_features.csv", X_train)
    np.savetxt(data_path / "test_features.csv", X_test)
    np.savetxt(data_path / "train_labels.csv", y_train)
    np.savetxt(data_path / "test_labels.csv", y_test)

    return {
        "X_train": X_train,
        "X_test": X_test,
        "y_train": y_train,
        "y_test": y_test,
    }


if __name__ == "__main__":
    generate_data()
