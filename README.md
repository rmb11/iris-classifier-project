# Iris Classifier Django + ML Project

## Project Overview

For this project I’ll be building a data-driven Django web application using the MVC/MTV structure that integrates a simple machine learning model. It will handle user input, display predictions quickly and support authentication, logging and deployment to a Proxmox VM. The system will also be set up for future scalability. My application will use an Iris flower classification model so it needs to provide fast and accurate predictions, a secure and responsive interface and a clear separation between the ML logic and Django web views.

---

## Model Research and Justification

I chose the Iris dataset for this project because it is a simple and well known multi-class classification problem that is small, fast to train and easy to explain. The model will use four numeric inputs (sepal length, sepal width, petal length and petal width) to predict the Iris species (setosa, versicolor or virginica). 

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

The MVP for this project will meet these goals:

- Accept user input for Iris flower measurements (four numeric features).
- Provide accurate predictions of the Iris species.
- Target a response time under one second per prediction.
- Give a clear and understandable prediction output.
- Provide real-time feedback to the user when they submit their input.
- Keep the ML logic in the `ml/` module separate from Django views.
- Use Streamlit as the main interface for entering data and viewing predictions.
- Log basic prediction activity (such as when predictions are made) to support later auditing and optimisation using the planned logging decorator.

---

## Progress Update – 25/11/2025

- Began development of Stage **8.2 – Data Ingestion and Preparation**.
- Implemented a basic Streamlit interface to collect four Iris flower measurements.
- Connected input values directly to the placeholder `predict()` function in `ml/predict.py`.
- Used Streamlit number inputs to check valid numeric input.
- Confirmed successful end-to-end flow. 
- Prediction currently uses placeholder logic and will be replaced with a trained model under **Stage 8.3**.

---

## Project Folder Structure

The project folder structure follows the required layout from the assessment:

```text
project_root/
│
├── ml/  # Machine Learning utilities (loading, inference, version control)
│   └── predict.py  #Inference entry point for the Iris model
│
├── classifier/  # Django app: forms, views, serializers
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── forms.py
│   └── templates/classifier/  # HTML templates for user forms and result pages
│       └── results.html
│
├── api/  # Django REST Framework endpoints (optional, for later stages)
│   ├── (views.py)
│   ├── (serializers.py)
│   └── (urls.py)
│
├── logs/  # Custom logging and prediction audit trail
│   └── app.log
│
├── docs/  # Project journal and documentation
│   └── journal.md
│
├── config/  # Django project settings and URL configuration
│
├── manage.py
└── requirements.txt