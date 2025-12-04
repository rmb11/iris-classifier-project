from django.urls import path
from . import views

urlpatterns = [
    path("api/predict/", views.predict_api, name="predict_api"),
]