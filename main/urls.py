from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("about/", views.AboutView.as_view(), name="about"),
    path("", views.HomePageView.as_view(), name="homepage"),
]
