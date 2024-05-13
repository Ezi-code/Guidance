from django.urls import path
from accounts.views import LoginView, LogoutView, StaffLoginView, StaffLogoutView

app_name = "accounts"

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("staff/login/", StaffLoginView.as_view(), name="staff_login"),
    path("staff/logout/", StaffLogoutView.as_view(), name="staff_logout"),
]
