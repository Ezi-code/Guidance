from django.contrib import admin
from staff.models import Session, Professional


class SessionAdmin(admin.ModelAdmin):
    list_display = ["student", "date"]
    list_filter = ["date"]
    search_fields = ["student", "date"]


class ProfessionalAdmin(admin.ModelAdmin):
    list_display = ["name", "service_type", "is_available"]
    list_filter = ["service_type", "is_available"]
    search_fields = ["name", "email", "phone", "service_type"]


admin.site.register(Session, SessionAdmin)
admin.site.register(Professional, ProfessionalAdmin)
