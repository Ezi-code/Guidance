from django.db import models
from datetime import datetime
from django.utils import timezone
from django.conf import settings


# Create your models here.
class Appointment(models.Model):
    class Service(models.TextChoices):
        GUIDANCE = "GUIDANCE", "Guidance"
        COUNSELLING = "COUNSELLING", "Counselling"

    class Status(models.TextChoices):
        ACCEPTED = ("ACCEPTED", "Accepted")
        DRAFT = ("DRAFT", "Draft")

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
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
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.DRAFT
    )

    def __str__(self) -> str:
        return f"{self.fname} --> {self.service_type}"


class Notifications(models.Model):
    class Status(models.TextChoices):
        ACTIVE = ("ACTIVE", "Active")
        READ = ("READ", "Read")

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_index=True
    )
    context = models.CharField(max_length=250)
    time_stamp = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=50, choices=Status.choices, default=Status.ACTIVE
    )

    class Meta:
        ordering = ("-time_stamp",)

    def __str__(self):
        return self.pk
