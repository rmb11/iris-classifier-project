# Iris Classifier Django + ML Project

## Project Overview

This project is a data-driven Django web application built using the MVC/MTV architecture that integrates a simple machine learning model. It handles user input, provides fast prediction responses and includes authentication and logging features. The application uses an Iris flower classification model and demonstrates a clear separation between the machine learning logic and Django web views.

---

## Model Research and Justification

I chose the Iris dataset for this project because it's a simple and well known multi-class classification problem that is small, fast to train and easy to explain. The model uses four numeric inputs (sepal length, sepal width, petal length and petal width) to predict the Iris species (setosa, versicolor or virginica). 

- **Problem & Dataset Source**  
  - Predict species using numeric measurements.  
  - Dataset from the UCI Machine Learning Repository https://archive.ics.uci.edu/dataset/53/iris

- **Chosen Algorithm**  
  - Likely Logistic Regression or similar due to simplicity and suitability for structured numeric data.

- **Strengths**  
  - Lightweight, high accuracy, interpretable, low computational cost.

- **Limitations**  
  - Not suited to complex datasets or larger-scale real-world systems.

- **Model Versioning Plan**  
  - Model will be saved using `joblib` and versioned separately so previous files are retained.

---

## Minimum Viable Product (MVP)

The completed MVP meets the following goals:

- Accept user input for Iris flower measurements (four numeric features).
- Provide accurate predictions of the Iris species.
- Target a response time under one second per prediction.
- Give a clear and understandable prediction output.
- Provide real-time feedback to the user when they submit their input.
- Keep the ML logic in the `ml/` module separate from Django views.
- Use Streamlit as the external interface for entering data and viewing predictions.
- Log prediction activity to support auditing. 

---

## Project Structure

```text
project_root/
├── classifier/ # Main Django app (views, models, templates)
├── config/ # Django project settings and URL configuration
├── docs/ # Project journal and documentation
├── logs/ # Application logs and prediction audit trail
├── ml/  # Machine learning logic (model loading and inference)
├── streamlit_app.py # Streamlit user interface
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md