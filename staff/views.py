from django.shortcuts import render, redirect
from django.views.generic import View
from staff.models import Session, AvailabelDates
from student.models import Appointment
from staff.services import LoginMixin
from django.contrib import messages


# Create your views here.
class Home(LoginMixin, View):
    def get(self, request):
        appointments = Appointment.objects.filter(status="DRAFT").all()
        ctx = {"appointments": appointments}
        return render(request, "staff/index.html", ctx)

    def post(self, request):
        appointment_id = int(request.POST.get("id"))
        # print(type(appointment_id))
        appointment = Appointment.objects.get(id=appointment_id)
        appointment.status = "ACCEPTED"
        appointment.save()
        new_session = Session.objects.create(student=appointment)
        new_session.save()
        messages.success(request, "Appointment Accepted")
        return redirect("staff:home")


class CreateAvailabeDate(LoginMixin, View):
    def get(self, request):
        dates = AvailabelDates.objects.all()
        ctx = {"dates": dates}
        return render(request, "staff/add_dates.html", ctx)

    def post(self, request):
        date = request.POST.get("date")
        time = request.POST.get("time")
        new_date = AvailabelDates.objects.create(date=date, time=time)
        new_date.full_clean()
        new_date.save()
        messages.success(request, "Date Added")
        return redirect("staff:add_dates")


class DeleteDate(LoginMixin, View):
    def post(self, request):
        date_id = int(request.POST.get("id"))
        date = AvailabelDates.objects.get(id=date_id)
        date.delete()
        messages.success(request, "Date Deleted")
        return redirect("staff:add_dates")


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
