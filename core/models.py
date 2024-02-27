from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Guidance(models.Model):
    class Service(models.TextChoices):
        GUIDANCE = "GUIDANCE", "Guidance"
        COUNSELLING = "COUNSELLING", "Counselling"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=False, null=False)
    level = models.CharField(max_length=10, blank=False, null=False)
    service_type = models.CharField(max_length=50, blank=False, null=False)
    department = models.CharField(max_length=150, blank=False, null=False)
    reason = models.TextField(null=False, blank=False)
    date_booked = models.DateField(
        editable=False,
        default=timezone.now,
    )

    def __str__(self) -> str:
        return f"{self.fname} --> {self.service_type}"
