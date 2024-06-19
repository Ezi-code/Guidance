from django.urls import path
from . import views

app_name = "api_service"

urlpatterns = [
    path("calendar/", views.calendar, name="calendar"),
    path("calendar/auth/", views.initiate_auth, name="initiate_auth"),
    path("oauth2callback/", views.oauth_callback, name="oauth_call2back"),
]
