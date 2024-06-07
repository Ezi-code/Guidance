from django import forms
from accounts.models import User
from typing import Any
from student.models import Appointment


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "email", "phone", "password")


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
        widgets = {
            "full_name": forms.TextInput(attrs={"placeholder": "Full Name"}),
            "email": forms.TextInput(attrs={"placeholder": "example@mail.com"}),
            "phone": forms.TextInput(attrs={"placeholder": "Phone number"}),
            "level": forms.TextInput(attrs={"placeholder": "Level"}),
            "service_type": forms.TextInput(
                attrs={"placeholder": "Service type (guidance/coucelling)"}
            ),
            "professional": forms.Select(),
            "department": forms.TextInput(attrs={"placeholder": "Department"}),
            "reason": forms.Textarea(attrs={"placeholder": "Reason fro session"}),
        }

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
