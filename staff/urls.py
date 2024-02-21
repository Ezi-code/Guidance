from django.urls import path
from staff.views import Home


app_name = "staff"

urlpatterns = [path("", Home.as_view(), name="home")]
