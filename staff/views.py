from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.views.generic.list import ListView
from student.models import Appointment
from staff.services import LoginMixin, send_email_notification
from django.contrib import messages
from django.utils import timezone
from forms import CaseManagementPrgressForm as CMPF, ClientRefferalForm
from accounts.models import User
from staff.models import CaseManagementPrgressNotes, ClientReferral
from api_service.calendar import main
from django.contrib.auth import get_user_model


class Home(LoginMixin, View):
    def get(self, request):
        appointments = Appointment.objects.filter(
            professional__name=request.user.username, status="DRAFT"
        ).all()
        context = {"appointments": appointments}
        return render(request, "staff/requests.html", context)


class AppointmentsView(LoginMixin, View):
    def get(self, request):
        appointments = Appointment.objects.filter(
            professional__name=request.user.username, status="ACCEPTED"
        ).all()
        context = {"appointments": appointments}
        return render(request, "staff/appointments.html", context)

    def post(self, request):
        appointment_id = int(request.POST.get("id"))
        appointment = Appointment.objects.get(id=appointment_id)
        appointment.status = "COMPLETED"
        appointment.save()
        send_email_notification.send_appointemt_completed_email(appointment)
        messages.success(request, "Appointment marked as Completed")
        return redirect("staff:appointments")


class CompletedSessionsView(LoginMixin, ListView):
    template_name = "staff/completed.html"
    model = Appointment
    context_object_name = "completed_tasks"

    def get_queryset(self):
        completed_tasks = Appointment.objects.filter(
            professional__name=self.request.user.username, status="COMPLETED"
        )
        return completed_tasks


class AppointmentRequestView(LoginMixin, View):
    def get(self, request):
        requests = Appointment.objects.filter(
            professional__name=request.user.username, status="DRAFT"
        )
        context = {"requests": requests}
        return render(request, "staff/requests.html", context)

    def post(self, request):
        request_id = request.POST.get("request-id")
        date = request.POST.get("date")
        time = request.POST.get("time")
        appointment = Appointment.objects.get(id=request_id)
        if Appointment.objects.filter(
            user=appointment.user,
            professional__name=request.user.username,
            status="ACCEPTED",
        ).exists():
            messages.error(request, "An appointment with this client already exist!")
            return redirect("staff:requests")
        appointment.session_date = date
        appointment.session_time = time
        appointment.status = "ACCEPTED"
        appointment.save()
        main(request, appointment)
        messages.success(request, "Request accepted")
        return redirect("staff:requests")


class ClientProgrssView(LoginMixin, View):
    def get(self, request):
        form = CMPF()
        client_id = request.GET.get("client_id")
        appointment_id = request.GET.get("appointment_id")
        context = {
            "form": form,
            "client_id": client_id,
            "appointment_id": appointment_id,
        }
        return render(request, "staff/progress_form.html", context)

    def post(self, request):
        client_id = request.POST.get("client_id")
        appointment_id = request.POST.get("appointment_id")
        next_date = request.POST.get("date")
        next_time = request.POST.get("time")
        appointment = Appointment.objects.get(id=appointment_id)
        client = get_object_or_404(User, id=client_id)
        form = CMPF(request.POST)
        print("validating form...")
        if form.is_valid():
            print("form calidation started...")
            form.instance.client = client
            form.instance.counsellor_name = request.user
            form.instance.appointment = appointment
            if next_date and next_time:
                form.instance.next_date = next_date
                form.instance.next_time = next_time
            form.full_clean()
            form.save()
            print("form validation successful...")
            messages.success(request, "Session notes saved! ")
            return redirect("staff:single_request", pk=appointment_id)
        print("form validation failed...")
        messages.error(request, "Error saving notes")
        return redirect("staff:single_request", pk=appointment_id)


class IndividualRequestsView(LoginMixin, View):
    def get(self, request, pk):
        appointment = Appointment.objects.get(id=pk)
        client = appointment.user
        context = {
            "client": client,
            "appointment": appointment,
        }
        return render(request, "staff/single_requests.html", context)


class CompletedSessions(LoginMixin, View):
    def get(self, request, uuid):
        appointment_id = request.GET.get("appointment_id")
        if appointment_id:
            compt_apmt = Appointment.objects.get(id=appointment_id)
            compt_apmt.status = "COMPLETED"
            compt_apmt.sav()
        past_sessions = Appointment.objects.filter(
            status="COMPLETED", professional__name=request.user.username
        )
        context = {"past_sessions": past_sessions}
        return render(request, "staff/previous_sessions.html", context)


class ClientReferralView(ListView, View):
    def post(self, request):
        form = ClientRefferalForm(request.POST)
        client_id = request.POST.get("client_id")
        user = User.objects.get(id=client_id)

        if form.is_valid():
            appointment = Appointment.objects.get(
                user=user, status="ACCEPTED", professional__name=request.user.username
            )
            appointment.status = "REFFERED"
            appointment.refferal_reason = form.data["reason"]
            appointment.reffered_counsellor = form.data["reffered_counsellor"]
            appointment.save()
            messages.success(request, "Client reffered")
            return redirect("staff:appointments")

        return redirect("staff:home")


class PreviousNotesView(LoginMixin, View):
    def get(self, request):

        client_id = request.GET.get("client_id")
        appointment_id = request.GET.get("appointment_id")

        notes = CaseManagementPrgressNotes.objects.filter(
            client_id=client_id,
            counsellor_name=request.user,
            appointment=appointment_id,
        )
        context = {"notes": notes}
        return render(request, "staff/previous_notes.html", context)


class CompleteTaskView(LoginMixin, View):
    def get(self, request):
        try:
            uuid = request.GET.get("appointment_id")
            appointment = Appointment.objects.get(id=uuid)
            appointment.status = "COMPLETED"
            appointment.save()
            return redirect("staff:appointments")
        except Exception as e:
            messages.error(request, "An error occured saving data!")
            return redirect("staff:apppointments")


class SinglePastSessionView(LoginMixin, View):
    def get(self, request, pk):
        try:
            appointment = Appointment.objects.get(id=pk)
            client = appointment.user
            context = {"appointment": appointment, "client": client}
            return render(request, "staff/past_single_client.html", context)
        except Exception as e:
            messages.error(request, "An error occured!")
            return redirect("staff:appointments")


class RefferalsView(LoginMixin, ListView):
    template_name = "staff/refferals.html"
    model = Appointment
    context_object_name = "reffered_clients"

    def get_queryset(self):
        reffered_clients = Appointment.objects.filter(
            professional__name=self.request.user.username, status="REFFERED"
        )
        return reffered_clients


class AcceptRefferal(LoginMixin, View):
    def get(self, request):
        id = request.GET.get("client_id")
        if id:
            appointment = Appointment.objects.get(id=id)
            appointment.status = "ACCEPTED"
            appointment.professional__name = request.user.username
            appointment.save()
            messages.success(request, "Refferal accepted")
            return redirect("staff:refferals")
        messages.error(request, "An error occured")
        return redirect("staff:refferals")


class ReffereClientView(LoginMixin, View):
    def get(self, request, uuid):
        client_id = uuid
        ctx = {"client_id": client_id}
        return render(request, "staff/client_referral_form.html", ctx)
