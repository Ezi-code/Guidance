from django.db import models
from django.utils import timezone


class Professional(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    service_type = models.CharField(max_length=150, null=True, blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Session(models.Model):
    student = models.ForeignKey(
        "student.Appointment", on_delete=models.CASCADE, default=None
    )
    date = models.DateTimeField(default=timezone.now)
