from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from student.models import Appointment, Notifications, Professional
from django.views.generic.base import TemplateView
from student.services import LoginMixin
from .forms import BookingForm
from django.contrib import messages


class HomeView(TemplateView):
    template_name = "index.html"


class BookView(LoginMixin, FormView):
    template_name = "book.html"
    success_url = reverse_lazy("student:dashboard")
    form_class = BookingForm

    def form_valid(self, form):
        form.full_clean()
        form.save()
        messages.success(self.request, "Appointment booked successfully")
        return super().form_valid(form)


class DashboardView(LoginMixin, View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("student:appointment")
        else:
            return redirect("student:login")


class NotificationsView(LoginMixin, View):
    def get(self, request):
        notifications = Notifications.objects.filter(user=request.user).all()
        ctx = {
            "notifications": notifications,
        }
        return render(request, "notifications.html", ctx)


class CheckAppointmentView(LoginMixin, View):
    from student.models import Appointment

    def get(self, request):
        appointments = Appointment.objects.filter(status="ACCEPTED").all()
        ctx = {
            "appointments": appointments,
        }
        return render(request, "appointments.html", ctx)
