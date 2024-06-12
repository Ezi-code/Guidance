from django.contrib import admin
from accounts.models import User


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "username",
        "email",
        "is_active",
        "is_superuser",
        "is_staff",
        "is_student",
    ]
    search_fields = ["username", "email"]
    list_filter = ["is_staff", "is_active", "is_superuser", "is_student"]
    list_per_page = 20


admin.site.register(User, UserAdmin)
