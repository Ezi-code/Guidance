from django import forms
from accounts.models import User
from typing import Any
from student.models import Appointment
from staff.models import CaseManagementPrgressNotes, ClientReferral


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
            "faculty",
            "department",
            "program",
            "hall",
            "service_type",
            "professional",
            "reason",
        ]
        widgets = {
            "full_name": forms.TextInput(
                attrs={"placeholder": "Full Name", "class": "form-control"}
            ),
            "email": forms.TextInput(
                attrs={"placeholder": "example@mail.com", "class": "form-control"}
            ),
            "phone": forms.TextInput(
                attrs={"placeholder": "Phone number", "class": "form-control"}
            ),
            "level": forms.TextInput(
                attrs={"placeholder": "Level", "class": "form-control"}
            ),
            "service_type": forms.TextInput(
                attrs={
                    "placeholder": "Service type (guidance/coucelling)",
                    "class": "form-control",
                }
            ),
            "professional": forms.Select(attrs={"class": "form-control"}),
            "department": forms.TextInput(
                attrs={"placeholder": "Department", "class": "form-control"}
            ),
            "faculty": forms.TextInput(
                attrs={"placeholder": "Faculty", "class": "form-control"}
            ),
            "program": forms.TextInput(
                attrs={"placeholder": "Program of study", "class": "form-control"}
            ),
            "hall": forms.TextInput(
                attrs={"placeholder": "Hall of residence", "class": "form-control"}
            ),
            "reason": forms.Textarea(
                attrs={
                    "placeholder": "Relationsip problems, Accademic stress, etc...",
                    "class": "form-control",
                }
            ),
        }

    def cleaned_data(self):
        cleaned_data = self.clean()
        full_name = cleaned_data.get("full_name")
        email = cleaned_data.get("email")
        phone = cleaned_data.get("phone")
        level = cleaned_data.get("level")
        faculty = cleaned_data.get("faculty")
        program = cleaned_data.get("program")
        hall = cleaned_data.get("hall")
        service_type = cleaned_data.get("sevrvice_type")
        professional = cleaned_data.get("professional")
        department = cleaned_data.get("deaprtmanet")
        reason = cleaned_data.get("reason")
        return cleaned_data

    def save(self, commit: bool = True):
        if commit == False:
            return super().save()
        return super().save(commit)


class CaseManagementPrgressForm(forms.ModelForm):
    class Meta:
        model = CaseManagementPrgressNotes
        fields = [
            "counselling_session",
            "client_appearance",
            "problem_identity",
            "intervention",
            "recomendation",
            "next_date",
            "next_time",
        ]

        widgets = {
            "counselling_session": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Counselling Session",
                    "cols": 5,
                    "rows": 4,
                }
            ),
            "client_appearance": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Client Appearance",
                    "cols": 5,
                    "rows": 4,
                }
            ),
            "problem_identity": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Problem Identity",
                    "cols": 5,
                    "rows": 4,
                }
            ),
            "intervention": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Intervention",
                    "cols": 5,
                    "rows": 4,
                }
            ),
            "recomendation": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Recomendation/Assignment",
                    "cols": 5,
                    "rows": 4,
                }
            ),
            "assignments": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "A",
                    "cols": 5,
                    "rows": 4,
                }
            ),
            "next_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "next_time": forms.TimeInput(
                attrs={
                    "class": "form-control",
                }
            ),
        }
