import streamlit as streamlit
import requests

# from ml.predict import predict

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
    # Extra validation to block any zero values (not realistic for Iris measurements)
    if (
        sepal_length == 0.0
        or sepal_width == 0.0
        or petal_length == 0.0
        or petal_width == 0.0
    ):
        streamlit.warning(
            "Please enter realistic measurements. None of the values should be zero."
        )
    else:
        # Build the data to send to Django
        payload = {
            "sepal_length": sepal_length,
            "sepal_width": sepal_width,
            "petal_length": petal_length,
            "petal_width": petal_width,
        }

        try:
            # Send the data to the Django API
            response = requests.post(
                "http://127.0.0.1:8000/api/predict/",
                json=payload,
            )

            # If Django returnns ok then show the prediction
            if response.status_code == 200:
                data = response.json()
                prediction = data.get("prediction")
                streamlit.success(f"Prediction: {prediction}")
            else:
                # If something goes wrong on Django side show the error
                streamlit.error(
                    f"API error: {response.status_code} - {response.text}"
                )
        except requests.exceptions.RequestException as exc:
            # If can't reach the Django server show this message
            streamlit.error(f"Could not reach prediction API: {exc}")