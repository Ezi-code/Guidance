from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic.list import ListView
from staff.models import Session
from student.models import Appointment
from staff.services import LoginMixin
from django.contrib import messages
from django.utils import timezone
from forms import CaseManagementPrgressForm as CMPF


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
        print(ses_time)
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
        print(request_id)
        return render(request, "staff/requests.html")


class ClientProgrssView(LoginMixin, View):
    def get(self, request):
        form = CMPF()
        ctx = {"form": form}
        return render(request, "staff/progress_form.html", ctx)

    def post(self, request):
        form = CMPF(request.post)
        if form.is_valid():
            form.full_clean()
            form.save()
            messages.success(request, "Session notes saved! ")
            return redirect()
        return render(request, "staff/progress_form.html", ctx)


class SingeleRequests(LoginMixin, View):
    def get(self, request):
        return render(request, "staff/single_request.html")

    # def post(self, request):
    #     return re
