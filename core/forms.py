from django import forms
from core.models import Appointment

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = "__all__"
        