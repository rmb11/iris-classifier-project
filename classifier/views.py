import json

from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from classifier.services.logging import action_logger
from django.shortcuts import render, redirect
from ml.predict import predict

@login_required
def home(request):
    return render(request, "classifier/home.html")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/accounts/login/")
    else:
        form = UserCreationForm()

    return render(request, "registration/register.html", {"form": form})

@staff_member_required
def logs_view(request):
    return JsonResponse({"message": "Staff can access logs here."})

@csrf_exempt
@action_logger
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