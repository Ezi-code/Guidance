from django.urls import path
from core.views import (
    HomeView,
    BookView,
    DashboardView,
    CheckAppointmentView,
    NotificationsView,
)

app_name = "core"

urlpatterns = [
    path("home", HomeView.as_view(), name="home"),
    path("book", BookView.as_view(), name="book"),
    path("dashboard", DashboardView.as_view(), name="dashboard"),
    path("appointment", CheckAppointmentView.as_view(), name="appointment"),
    path("notifications", NotificationsView.as_view(), name="notifications"),
]
