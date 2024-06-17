from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.core.mail import EmailMessage
from django.conf import settings


class LoginMixin(LoginRequiredMixin):
    def get_login_url(self):
        return reverse_lazy("accounts:staff_login")


class SendEmailNotificatio:
    def send_appointemt_accepted_email(self, appointment):
        email = EmailMessage(
            subject="Appointment Accepted",
            body=f"Your appointment has been accepted by {appointment.professional.name}",
            to=[appointment.email],
            from_email=settings.EMAIL_HOST_USER,
        )
        email.send()
        return email

    def send_appointemt_completed_email(self, appointment):
        email = EmailMessage(
            subject="Appointment Completed",
            body=f"Your appointment has been completed by {appointment.professional.name}",
            to=[appointment.user.email],
        )
        email.send()
        return email


send_email_notification = SendEmailNotificatio()
