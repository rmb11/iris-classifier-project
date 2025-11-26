"""
Prediction utilities for the Iris classifier.

This is a simple placeholder to test Streamlit 
before loading the real trained model from a joblib file.
"""

from typing import Literal

# Defining the three specific allowed output classes
IrisClass = Literal["setosa", "versicolor", "virginica"]

def predict(
    sepal_length: float,
    sepal_width: float,
    petal_length: float,
    petal_width: float,
) -> IrisClass:
    """
    Placeholder model for Iris classification.
    
    Uses basic conditional logic (petal dimensions) to simulate a 
    prediction for testing the application flow.
    
    Args:
        sepal_length (float): Length of the sepal in cm.
        sepal_width (float): Width of the sepal in cm.
        petal_length (float): Length of the petal in cm.
        petal_width (float): Width of the petal in cm.
        
    Returns:
        IrisClass: The predicted species ("setosa", "versicolor", or "virginica").
    """
    # Simple logic-based "prediction" using petal measurements
    if petal_length < 2.5:
        return "setosa"
    elif petal_width < 1.8:
        return "versicolor"
    else:
        return "virginica"