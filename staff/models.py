from django.db import models
from django.utils import timezone

# from student.models import Appointment


# Create your models here.
class AvailabelDates(models.Model):
    class Status(models.TextChoices):
        AVAILABLE = ("AVAILABLE", "Available")
        EXPIRED = ("EXPIRED", "Expired")

    date = models.DateField(default=timezone.localdate)
    time = models.TimeField(default=timezone.localtime)
    status = models.CharField(
        max_length=50, choices=Status.choices, default=Status.AVAILABLE
    )

    def __str__(self):
        return f"{self.date.date()} {self.date.time()}"


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
