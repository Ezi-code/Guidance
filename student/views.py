from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.urls import reverse_lazy
from student.models import Appointment, Notifications, Professional
from django.views.generic.base import TemplateView
from student.services import LoginMixin
from forms import BookingForm
from django.contrib import messages
from django.utils import timezone
from datetime import datetime


datetime.date


class HomeView(TemplateView):
    template_name = "student/index.html"


class BookView(LoginMixin, View):
    template = "student/booking_form.html"
    success_url = reverse_lazy("student:requests")
    form_class = BookingForm()

    def get(self, request):
        professionals = Professional.objects.all()
        ctx = {
            "form": self.form_class,
            "professionals": professionals,
        }
        return render(request, self.template, ctx)

    def post(self, request):
        form = BookingForm(request.POST)
        print(form.data)
        print("In try block")
        if form.is_valid():
            print("form is valid")
            form.instance.request_date = timezone.now()
            form.instance.user = request.user
            form.save()
            messages.success(request, "Appointment booked successfylly")
            return redirect("student:dashboard")
        else:
            messages.error(request, "An error occured")
            print("Out of try block")
            return redirect("student:book")


class CompletedSessionsView(LoginMixin, View):
    def get(self, request):
        comp_sessions = Appointment.objects.filter(status="COMPLETED").all()
        ctx = {
            "comp_sessions": comp_sessions,
        }
        return render(request, "student/completed.html", ctx)


class AppointmentsView(LoginMixin, View):
    from student.models import Appointment

    def get(self, request):
        appointments = Appointment.objects.filter(
            user=request.user, status="DRAFT"
        ).all()
        ctx = {
            "appointments": appointments,
        }
        return render(request, "student/appointments.html", ctx)


class RequestsView(LoginMixin, View):
    def get(self, request):
        requests = Appointment.objects.filter(status="DRAFT").all()
        ctx = {"requests": requests}
        return render(request, "student/requests.html", ctx)
