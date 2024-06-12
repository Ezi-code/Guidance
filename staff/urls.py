from django.urls import path
from staff import views


app_name = "staff"

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("appointments", views.AppointmentsView.as_view(), name="appointments"),
    path("completed", views.CompletedView.as_view(), name="completed"),
    path("requests", views.RequestsView.as_view(), name="requests"),
    path("client", views.ClientProgrssView.as_view(), name="client_progress"),
    path("single-request", views.SingeleRequests.as_view(), name="single_request"),
]
