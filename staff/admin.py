from django.contrib import admin
from staff.models import AvailabelDates, Session

# Register your models here.
admin.site.register([AvailabelDates, Session])
