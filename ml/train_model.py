"""
Train a simple Iris classification model.
It uses scikit-learn's built-in Iris dataset and Logistic Regression.
"""

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
from pathlib import Path


def main() -> None:
    """
    Trains and evaluates two simple ML models on the Iris dataset.
    The best-performing model is saved using joblib for later use.
    """
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

    accuracy = model.score(X_test, y_test)
    print(f"LogisticRegression accuracy: {accuracy:.3f}")
    
    # Optimisation - trying RandomForest
    rf_model = RandomForestClassifier(
        n_estimators=100,
        random_state=42,
    )
    rf_model.fit(X_train, y_train)

    rf_accuracy = rf_model.score(X_test, y_test)
    print(f"RandomForest accuracy: {rf_accuracy:.3f}")
    
    # Pick the better model
    if rf_accuracy > accuracy:
        best_model = rf_model
        print("Using RandomForest as the optimised model.")
    else:
        best_model = model
        print("Keeping LogisticRegression as performance was equal or better.")

    # Save the trained model to the ml/ folder
    model_path = Path(__file__).with_name("iris_model.joblib")
    joblib.dump(best_model, model_path)
    print(f"Saved model to: {model_path}")


if __name__ == "__main__":
    main()