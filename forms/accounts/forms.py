from django import forms
from accounts.models import User


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "email", "phone", "password")
