from django.contrib import admin
from student.models import Appointment, Faculty, Department


# Register your models here.
class AdminAppointment(admin.ModelAdmin):
    list_display = ["full_name", "status", "session_date"]
    search_fields = ["full_name", "status", "session_date"]


class AdminFaculty(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name", "department"]


class AdminDepartment(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


admin.site.register(Appointment, AdminAppointment)
admin.site.register(Faculty, AdminFaculty)
admin.site.register(Department, AdminDepartment)
