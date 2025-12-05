from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("api/predict/", views.predict_api, name="predict_api"),
    path("logs/", views.logs_view, name="logs_view"),
    path("register/", views.register, name="register"),
]