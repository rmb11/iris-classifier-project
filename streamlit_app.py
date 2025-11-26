import streamlit as streamlit

from ml.predict import predict

streamlit.set_page_config(
    page_title="Iris Classifier",
    layout="centered",
)

streamlit.title("Iris Species Classifier")
streamlit.write(
    "Enter the four Iris measurements below to get a predicted species."
)

# --- Input Form ---
sepal_length = streamlit.number_input(
    "Sepal length (cm)",
    min_value=0.0,
    max_value=10.0,
    value=0.0,
    step=0.1,
)

sepal_width = streamlit.number_input(
    "Sepal width (cm)",
    min_value=0.0,
    max_value=10.0,
    value=0.0,
    step=0.1,
)

petal_length = streamlit.number_input(
    "Petal length (cm)",
    min_value=0.0,
    max_value=10.0,
    value=0.0,
    step=0.1,
)

petal_width = streamlit.number_input(
    "Petal width (cm)",
    min_value=0.0,
    max_value=10.0,
    value=0.0,
    step=0.1,
)

if streamlit.button("Predict"):
    try:
        prediction = predict(
            sepal_length=sepal_length,
            sepal_width=sepal_width,
            petal_length=petal_length,
            petal_width=petal_width,
        )
        streamlit.success(f"Prediction: {prediction}")
    except Exception as exc:
        streamlit.error(f"Something went wrong while predicting: {exc}")