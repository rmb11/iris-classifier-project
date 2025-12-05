import json

from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from django.contrib.admin.views.decorators import staff_member_required
from ml.predict import predict

@staff_member_required
def logs_view(request):
    return JsonResponse({"message": "Staff can access logs here."})

@csrf_exempt
def predict_api(request):
    # This API only works with POST
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])

    # Try to read JSON that Streamlit sends
    try:
        payload = json.loads(request.body or "{}")
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON payload.")

    # Get the four iris values from the JSON
    sepal_length = payload.get("sepal_length")
    sepal_width = payload.get("sepal_width")
    petal_length = payload.get("petal_length")
    petal_width = payload.get("petal_width")

    # Make sure the user actually sent all four numbers.
    if None in (sepal_length, sepal_width, petal_length, petal_width):
        return JsonResponse(
            {"error": "All four iris values are required."},
            status=400,
        )

    # Call the ML model to get the prediction.
    # Convert values to floats because the model expects numbers.
    prediction = predict(
        float(sepal_length),
        float(sepal_width),
        float(petal_length),
        float(petal_width),
    )

    # Send the prediction back to Streamlit as JSON.
    return JsonResponse({"prediction": prediction})