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


class Session(models.Model):
    student = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
