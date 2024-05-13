from django.contrib import admin
from staff.models import AvailabelDates, Session, Professional


# Register your models here.
class AvailabelDatesAdmin(admin.ModelAdmin):
    list_display = ["date", "time", "status"]
    list_filter = ["date", "status"]
    search_fields = ["date", "status"]


class SessionAdmin(admin.ModelAdmin):
    list_display = ["student", "date"]
    list_filter = ["date"]
    search_fields = ["student", "date"]


class ProfessionalAdmin(admin.ModelAdmin):
    list_display = ["name", "service_type", "is_available"]
    list_filter = ["service_type", "is_available"]
    search_fields = ["name", "email", "phone", "service_type"]


admin.site.register(AvailabelDates, AvailabelDatesAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(Professional, ProfessionalAdmin)
