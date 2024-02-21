from django.urls import path
from core.views import HomeView, BookView, LoginView, DashboardView, LogoutView

app_name = "core"

urlpatterns = [
    path("home", HomeView.as_view(), name="home"),
    path("book", BookView.as_view(), name="book"),
    path("login", LoginView.as_view(), name="login"),
    path("dashboard", DashboardView.as_view(), name="dashboard"),
    path("logout", LogoutView.as_view(), name="logout"),
]
