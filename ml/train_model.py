"""
Train a simple Iris classification model and save it to disk.

This script is for Stage 8.3 (Model Training, Serialisation and Versioning).
It uses scikit-learn's built-in Iris dataset and Logistic Regression.
"""

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib
from pathlib import Path


def main() -> None:
    # Load Iris dataset (from scikit-learn, originally from UCI)
    iris = load_iris()
    X = iris.data  # 4 input features
    y = iris.target  # class labels

    # Split into train/test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train a Logistic Regression classifier
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)

    # Print simple accuracy for understanding
    accuracy = model.score(X_test, y_test)
    print(f"Test accuracy: {accuracy:.3f}")

    # Save the trained model to the ml/ folder
    model_path = Path(__file__).with_name("iris_model.joblib")
    joblib.dump(model, model_path)
    print(f"Saved model to: {model_path}")


if __name__ == "__main__":
    main()