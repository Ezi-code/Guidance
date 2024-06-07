from typing import Any
from django import forms
from student.models import Appointment


class BookingForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            "full_name",
            "email",
            "phone",
            "level",
            "service_type",
            "professional",
            "department",
            "reason",
        ]

    def cleaned_data(self):
        cleaned_data = self.clean()
        full_name = cleaned_data.get("fname")
        email = cleaned_data.get("email")
        phone = cleaned_data.get("phone")
        level = cleaned_data.get("level")
        service_type = cleaned_data.get("sevrvice_type")
        professional = cleaned_data.get("professional")
        department = cleaned_data.get("deaprtmanet")
        reason = cleaned_data.get("reason")
        return cleaned_data

    def save(self, commit: bool = True):
        if commit == False:
            return super().save()
        return super().save(commit)
