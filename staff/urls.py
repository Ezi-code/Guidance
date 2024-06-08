from django.urls import path
from staff import views


app_name = "staff"

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("appointments", views.Appointemtns.as_view(), name="appointments"),
]
