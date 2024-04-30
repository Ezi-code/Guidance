from django.db import models
from django.utils import timezone
from core.models import Appointment


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


class Staff(models.Model):
    staff_id = models.CharField(unique=True, max_length=50, primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    available_dates = models.ForeignKey(AvailabelDates, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class Session(models.Model):
    name = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    date = models.ForeignKey(AvailabelDates, on_delete=models.CASCADE)
