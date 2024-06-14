from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.views.generic.list import ListView
from staff.models import Session
from student.models import Appointment
from staff.services import LoginMixin
from django.contrib import messages
from django.utils import timezone
from forms import CaseManagementPrgressForm as CMPF, ClientRefferalForm
from accounts.models import User
from staff.models import CaseManagementPrgressNotes


class Home(LoginMixin, View):
    def get(self, request):
        appointments = Appointment.objects.filter(
            professional__name=request.user.username, status="DRAFT"
        ).all()
        ctx = {"appointments": appointments}
        return render(request, "staff/index.html", ctx)

    def post(self, request):
        #
        ses_date = request.POST.get("session_date")
        ses_time = request.POST.get("session_time")
        appointment_id = int(request.POST.get("id"))
        #
        appointment = Appointment.objects.get(id=appointment_id)
        appointment.status = "ACCEPTED"
        appointment.response_date = timezone.now()
        appointment.session_date = ses_date
        appointment.session_time = ses_time
        #
        appointment.save()
        new_session = Session.objects.create(student=appointment)
        new_session.save()
        messages.success(request, "Appointment Accepted")
        return redirect("staff:home")


class AppointmentsView(LoginMixin, View):
    def get(self, request):
        appointments = Appointment.objects.filter(
            professional__name=request.user.username, status="ACCEPTED"
        ).all()
        ctx = {"appointments": appointments}
        return render(request, "staff/appointments.html", ctx)

    def post(self, request):
        appointment_id = int(request.POST.get("id"))
        appointment = Appointment.objects.get(id=appointment_id)
        appointment.status = "COMPLETED"
        appointment.save()
        messages.success(request, "Appointment marked as Completed")
        return redirect("staff:appointments")


class CompletedView(LoginMixin, ListView):
    template_name = "staff/completed.html"
    model = Appointment
    context_object_name = "completed_tasks"
    paginate_by = 10

    def get_queryset(self):
        completed_tasks = Appointment.objects.filter(
            professional__name=self.request.user.username, status="COMPLETED"
        )
        return completed_tasks


class RequestsView(LoginMixin, View):
    def get(self, request):
        requests = Appointment.objects.filter(
            professional__name=request.user.username, status="DRAFT"
        )
        ctx = {"requests": requests}
        return render(request, "staff/requests.html", ctx)

    def post(self, request):
        request_id = request.POST.get("request-id")
        date = request.POST.get("date")
        time = request.POST.get("time")
        appointment = Appointment.objects.get(id=request_id)
        appointment.session_date = date
        appointment.session_time = time
        appointment.status = "ACCEPTED"
        appointment.save()
        return render(request, "staff/requests.html")


class ClientProgrssView(LoginMixin, View):
    def get(self, request):
        form = CMPF()
        client_id = request.GET.get("client_id")
        appointment_id = request.GET.get("appointment_id")
        ctx = {"form": form, "client_id": client_id, "appointment_id": appointment_id}
        return render(request, "staff/progress_form.html", ctx)

    def post(self, request):
        client_id = request.POST.get("client_id")
        appointment_id = request.GET.get("appointment_id")
        appointment = Appointment.objects.get(id=appointment_id)
        client = get_object_or_404(User, id=client_id)
        form = CMPF(request.POST)
        if form.is_valid():
            form.instance.client = client
            form.instance.counsellor_name = request.user
            form.instance.appointment = appointment
            form.full_clean()
            form.save()
            messages.success(request, "Session notes saved! ")
            return redirect(
                "staff:single_request",
                uuid=client_id,
            )


class SingeleRequests(LoginMixin, View):
    def get(self, request, uuid):
        appointment_id = request.GET.get("appointment_id")
        client = get_object_or_404(User, id=uuid)
        appointment = Appointment.objects.filter(
            id=appointment_id, user=client, status="ACCEPTED"
        ).first()
        ctx = {
            "client": client,
            "appointment": appointment,
        }
        return render(request, "staff/single_request.html", ctx)

    def post(self, request):
        return


class CompletedSessions(LoginMixin, View):
    def get(self, request, uuid):
        appointment_id = request.GET.get("appointment_id")
        if appointment_id:
            compt_apmt = Appointment.objects.get(id=appointment_id)
            compt_apmt.status = "COMPLETED"
            compt_apmt.sav()
        past_sessions = Appointment.objects.filter(
            status="COMPLETED", professional__name=request.user, user__id=uuid
        )
        ctx = {"past_sessions": past_sessions}
        return render(request, "staff/previous_sessions.html", ctx)

    def post(self, request):
        pass


class ClientReferralView(ListView, View):
    def post(self, request):
        form = ClientRefferalForm(request.POST)
        client_id = form.data["client_id"]
        appointment = Appointment.objects.get(
            user_id=client_id,
            professional__name=request.user,
            status="ACCEPTED",
        )

        if form.is_valid():
            form.instance.counsellor_id = request.user.id
            form.instance.client_id = form.data["client_id"]
            form.instance.reffered_by = request.user.username
            form.instance.counsellor_id = request.user.id
            form.instance.name = appointment.full_name
            form.instance.phone = appointment.phone
            form.save()
            messages.success(request, "Client reffered")
            return redirect("staff:home")

        return redirect("staff:home")


class PreviousNotes(LoginMixin, View):
    def get(self, request):

        client_id = request.GET.get("client_id")
        appointment_id = request.GET.get("appointment_id")

        notes = CaseManagementPrgressNotes.objects.filter(
            client_id=client_id,
            counsellor_name=request.user,
            appointment=appointment_id,
        )
        ctx = {"notes": notes}
        return render(request, "staff/previous_notes.html", ctx)

class CompleteTask(LoginMixin, View):
    def get(self, request):
        appointment_id = request.GET.get('appointment_id')
        appointment = Appointment.objects.get(id=appointment_id)
        appointment.status = 'COMPLETED'
        appointment.save()
        return redirect("staff:appointments")
