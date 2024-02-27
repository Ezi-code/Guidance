from django.db import models
from django.utils import timezone
from core.models import Guidance


# Create your models here.
class AvailabelDates(models.Model):
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.date.date()} {self.date.time()}"


class Staff(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    available_dates = models.ForeignKey(AvailabelDates, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class Session(models.Model):
    name = models.ForeignKey(Guidance, on_delete=models.CASCADE)
    date = models.ForeignKey(AvailabelDates, on_delete=models.CASCADE)
