from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.core.mail import EmailMessage
from django.conf import settings


class LoginMixin(LoginRequiredMixin):
    def get_login_url(self):
        return reverse_lazy("accounts:staff_login")


class SendEmailNotification:
    def send_appointemt_accepted_email(self, appointment, request):
        body = f"""Hello {appointment.full_name},
        Your appointment request for {appointment.reason} has been successfully accepted by {appointment.professional}.
        which will be on the {appointment.session_date} at {appointment.session_time}, at the guidance and counselling unit.

        thank You
        {request.user.username}
        """
        email = EmailMessage(
            subject="Appointment Accepted",
            body=body,
            to=[appointment.email],
            from_email=settings.EMAIL_HOST_USER,
        )
        email.send()
        return email

    def send_appointemt_completed_email(self, appointment):
        email = EmailMessage(
            subject="Appointment Completed",
            body=f"""Hello {appointment.full_name},
            Thank you for your time.
            Your appointment '{appointment.reason}' has been completed by {appointment.professional.name}.
            We hope your issue has been resolved and you are feeling better.
            Wish you all the best.
            Thank You

            {appointment.professional.name}
            """,
            to=[appointment.email],
        )
        email.send()
        return email


