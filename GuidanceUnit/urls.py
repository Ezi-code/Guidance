from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("student.urls", namespace="student")),
    path("staff/", include("staff.urls", namespace="staff")),
    path("accounts/", include("accounts.urls", namespace="accounts")),
    path("api/", include("api_service.urls", namespace="api_service")),
    path("main", include("main.urls", namespace="main")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
