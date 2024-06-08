from django.contrib import admin
from student.models import Appointment


# Register your models here.
class AdminAppointment(admin.ModelAdmin):
    list_display = ["full_name", "status", "session_date"]
    search_fields = ["full_name", "status", "session_date"]


admin.site.register(Appointment, AdminAppointment)
