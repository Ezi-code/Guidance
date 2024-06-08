from django.shortcuts import render, redirect
from django.views.generic import View
from staff.models import Session
from student.models import Appointment
from staff.services import LoginMixin
from django.contrib import messages
from django.utils import timezone


class Home(LoginMixin, View):
    def get(self, request):
        appointments = Appointment.objects.filter(status="DRAFT").all()
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


class Appointemtns(LoginMixin, View):
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
