from django import forms
from accounts.models import User


class RegisterForm:
    class Meta:
        model = User

    username = forms.CharField(max_length=100, label="User Name", strip=True)
    email = forms.EmailField(
        required=True,
        help_text="Enter a valid email address",
        show_hidden_initial=True,
    )
    password = forms.PasswordInput(render_value=False)
    confirm_pass = forms.PasswordInput(render_value=False)
