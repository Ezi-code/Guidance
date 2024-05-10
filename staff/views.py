from django.shortcuts import render, redirect
from django.views.generic import View
from staff.models import Session, AvailabelDates
from core.models import Appointment


# Create your views here.
class Home(View):
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
        return redirect("staff:home")


class CreateAvailabeDate(View):
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
        return redirect("staff:add_dates")


class DeleteDate(View):
    def post(self, request):
        date_id = int(request.POST.get("id"))
        date = AvailabelDates.objects.get(id=date_id)
        date.delete()
        return redirect("staff:add_dates")


class Appointemtns(View):
    def get(self, request):
        appointments = Appointment.objects.filter(status="ACCEPTED").all()
        ctx = {"appointments": appointments}
        return render(request, "staff/appointments.html", ctx)

    def post(self, request):
        appointment_id = int(request.POST.get("id"))
        appointment = Appointment.objects.get(id=appointment_id)
        print(appointment)
        # appointment.status = "COMPLETED"
        # appointment.save()
        return redirect("staff:appointments")
