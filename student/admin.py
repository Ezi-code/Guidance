from django.contrib import admin
from student.models import Appointment


# Register your models here.
class AdminAppointment(admin.ModelAdmin):
    list_display = ["full_name", "status", "date"]
    search_fields = ["full_name", "status", "date"]


admin.site.register(Appointment, AdminAppointment)
