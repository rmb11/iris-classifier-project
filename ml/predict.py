"""
Prediction utilities for the Iris classifier.

Loads trained model from 'iris_model.joblib' and uses it to make predictions.
"""

import joblib
import numpy as np
from typing import Literal
from pathlib import Path

# Define the allowed output classes
IrisClass = Literal["setosa", "versicolor", "virginica"]

# Path to the saved model
MODEL_PATH = Path(__file__).with_name("iris_model.joblib")

# Load model once at import time
_model = joblib.load(MODEL_PATH)

def predict(
    sepal_length: float,
    sepal_width: float,
    petal_length: float,
    petal_width: float,
) -> IrisClass:
    """
    Use the trained ML model to predict the Iris species.

    Args:
        sepal_length (float)
        sepal_width (float)
        petal_length (float)
        petal_width (float)

    Returns:
        IrisClass: one of "setosa", "versicolor", "virginica"
    """
    # Prepare a new sample for prediction
    sample = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

    # Predict using the trained model
    prediction_numeric = _model.predict(sample)[0]

    # Convert numeric prediction (0,1,2) to string label
    class_names = ["setosa", "versicolor", "virginica"]
    return class_names[prediction_numeric]