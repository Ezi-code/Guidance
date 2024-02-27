from django.contrib import admin
from staff.models import Staff, AvailabelDates

# Register your models here.
admin.site.register([Staff, AvailabelDates])
