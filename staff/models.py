from django.db import models
from django.utils import timezone
from accounts.models import User


class Professional(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    service_type = models.CharField(max_length=150, null=True, blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class CaseManagementPrgressNotes(models.Model):

    client = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="client", default=None
    )
    appointment = models.ForeignKey(
        "student.Appointment", on_delete=models.CASCADE, default=None, related_name="appointment_notes"
    )
    counselling_session = models.TextField(blank=True, null=True)
    client_appearance = models.TextField()
    problem_identity = models.TextField()
    intervention = models.TextField()
    recomendation = models.TextField()
    assignments = models.TextField()
    next_date = models.DateField(blank=True, null=True)
    next_time = models.TimeField(blank=True, null=True)
    session_date = models.DateTimeField(default=timezone.now, editable=False)
    counsellor_name = models.CharField(max_length=100, blank=False)


class ClientReferral(models.Model):
    client = models.ForeignKey(User, on_delete=models.PROTECT, default=None)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    referred_by = models.CharField(max_length=100)
    counsellor_id = models.IntegerField()
    reason = models.TextField(max_length=1000, blank=True, null=True)
    date = models.DateField(default=timezone.now)
