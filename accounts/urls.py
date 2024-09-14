from django.urls import path
from accounts import views

app_name = "accounts"

urlpatterns = [
    path("student/register/", views.StudentRegisterView.as_view(), name="student_signup"),
    path("student/login/", views.StudentLoginView.as_view(), name="student_login"),
    path("student/logout/", views.StudentLogoutView.as_view(), name="student_logout"),
    path("staff/login/", views.StaffLoginView.as_view(), name="staff_login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path(
        "check-student-username/",
        views.student_check_username,
        name="student_check_username",
    ),
    path(
        "check-staff-username/", views.staff_check_username, name="check_staff_username"
    ),
]
