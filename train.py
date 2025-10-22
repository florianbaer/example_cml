from pathlib import Path

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import numpy as np


def load_dataset(data_dir: str | Path = "data"):
    """Load train/test features and labels from disk."""

    data_path = Path(data_dir)
    X_train = np.genfromtxt(data_path / "train_features.csv")
    y_train = np.genfromtxt(data_path / "train_labels.csv")
    X_test = np.genfromtxt(data_path / "test_features.csv")
    y_test = np.genfromtxt(data_path / "test_labels.csv")
    return X_train, y_train, X_test, y_test


def train_model(
    data_dir: str | Path = "data",
    max_depth: int = 2,
    random_state: int = 0,
    metrics_path: str | Path = "metrics.txt",
    plot_path: str | Path = "plot.png",
):
    """Train a RandomForest model and persist metrics and a confusion matrix plot."""

    X_train, y_train, X_test, y_test = load_dataset(data_dir)

    clf = RandomForestClassifier(max_depth=max_depth, random_state=random_state)
    clf.fit(X_train, y_train)

    acc = clf.score(X_test, y_test)

    metrics_output_path = Path(metrics_path)
    metrics_output_path.parent.mkdir(parents=True, exist_ok=True)
    metrics_output_path.write_text(f"Accuracy: {acc:.6f}\n", encoding="utf-8")

    disp = ConfusionMatrixDisplay.from_estimator(
        clf, X_test, y_test, normalize="true", cmap=plt.cm.Blues
    )
    plot_output_path = Path(plot_path)
    plot_output_path.parent.mkdir(parents=True, exist_ok=True)
    disp.figure_.savefig(plot_output_path)
    plt.close(disp.figure_)

    return {
        "classifier": clf,
        "accuracy": acc,
        "display": disp,
    }


if __name__ == "__main__":
    results = train_model(max_depth=3)
    print(results["accuracy"])
