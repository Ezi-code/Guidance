from django.shortcuts import render, redirect
from django.views.generic import View
from django.urls import reverse_lazy
from student.models import Appointment, Department, Faculty, Professional
from student.services import LoginMixin
from forms import BookingForm
from django.contrib import messages
from django.utils import timezone


class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            if request.user.is_student:
                return render(request, "student/index.html")
            if request.user.is_staff:
                return redirect("staff:home")
        return render(request, "student/index.html")


class BookView(LoginMixin, View):
    template = "student/booking_form.html"
    success_url = reverse_lazy("student:requests")
    form_class = BookingForm()

    def get(self, request):
        professionals = Professional.objects.all()
        faculty = Faculty.objects.all()
        department = Department.objects.all()
        ctx = {
            "form": self.form_class,
            "professionals": professionals,
            "faculty": faculty,
            "department": department,
        }
        return render(request, self.template, ctx)

    def post(self, request):
        form = BookingForm(request.POST)
        if form.is_valid():
            form.instance.request_date = timezone.now()
            form.instance.user = request.user
            form.save()
            messages.success(request, "Appointment booked successfylly")
            return redirect("student:requests")
        else:
            messages.error(request, "An error occured")
            return redirect("student:book")


class CompletedSessionsView(LoginMixin, View):
    def get(self, request):
        comp_sessions = Appointment.objects.filter(status="COMPLETED").all()
        ctx = {
            "comp_sessions": comp_sessions,
        }
        return render(request, "student/completed.html", ctx)


class AppointmentsView(LoginMixin, View):
    def get(self, request):
        appointments = Appointment.objects.filter(
            status="ACCEPTED", user=request.user
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
