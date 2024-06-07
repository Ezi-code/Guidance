from django.urls import path
from student import views

app_name = "student"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("book", views.BookView.as_view(), name="book"),
    path("dashboard", views.DashboardView.as_view(), name="dashboard"),
    path("appointment", views.CheckAppointmentView.as_view(), name="appointment"),
    path("notifications", views.NotificationsView.as_view(), name="notifications"),
]
