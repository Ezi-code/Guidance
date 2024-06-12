from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class LoginMixin(LoginRequiredMixin):
    def get_login_url(self):
        return reverse_lazy("accounts:student_login")
