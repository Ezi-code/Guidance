from django.db import models
from datetime import datetime
from django.utils import timezone
from django.conf import settings
from staff.models import Professional
from accounts.models import User


# Create your models here.
class Appointment(models.Model):
    class Service(models.TextChoices):
        GUIDANCE = "GUIDANCE", "Guidance"
        COUNSELLING = "COUNSELLING", "Counselling"

    class Status(models.TextChoices):
        ACCEPTED = ("ACCEPTED", "Accepted")
        DRAFT = ("DRAFT", "Draft")
        COMPLETED = ("COMPLETED", "Completed")
        REFERRED = ("REFFERED", "Reffered")

    user = models.ForeignKey(User, on_delete=models.PROTECT, db_index=True, default=1)
    full_name = models.CharField(db_index=True, max_length=100, blank=False, null=False)
    email = models.EmailField(db_index=True)
    phone = models.CharField(max_length=15, blank=False, null=False, db_index=True)
    faculty = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=150, blank=False, null=False)
    program = models.CharField(max_length=100, blank=True, null=True, db_index=True)
    hall = models.CharField(max_length=100, blank=True, null=True, db_index=True)
    level = models.CharField(max_length=10, blank=False, null=False, db_index=True)
    service_type = models.CharField(
        max_length=50, blank=False, null=False, db_index=True
    )
    reason = models.TextField(null=False, blank=False, db_index=True)
    refferal_reason = models.TextField(blank=True, null=True)
    reffered_counsellor = models.IntegerField(null=True, blank=True)
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE, default=1)
    request_date = models.DateTimeField(blank=True, null=True)
    session_date = models.DateField(
        default=timezone.now,
    )
    session_time = models.TimeField(null=True, blank=True)
    response_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.DRAFT
    )

    def __str__(self) -> str:
        return "Appointment for {}".format(self.full_name)


class Department(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)


class Faculty(models.Model):
    name = models.CharField(max_length=150)
