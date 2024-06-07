from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from student.models import Appointment, Notifications, Professional
from django.views.generic.base import TemplateView
from student.services import LoginMixin
from forms import BookingForm
from django.contrib import messages


class HomeView(TemplateView):
    template_name = "student/index.html"


class BookView(LoginMixin, View):
    template = "student/book.html"
    success_url = reverse_lazy("student:dashboard")
    form_class = BookingForm()

    def get(self, request):
        professionals = Professional.objects.all()
        ctx = {"form": self.form_class, "professionals": professionals}
        return render(request, self.template, ctx)

    def post(self, request):
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Appointment booked successfylly")
            return redirect("student:dashboard")
        else:
            messages.error(request, "An error occured")
            return redirect("student:book")

    # def form_valid(self, form):
    #     form.full_clean()
    #     form.save()
    #     messages.success(self.request, "Appointment booked successfully")
    #     return super().form_valid(form)

    # def get_context_data(self, **kwargs):
    #     professionals = Professional.objects.all()
    #     return super().get_context_data(professionals)


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
        return render(request, "student/notifications.html", ctx)


class CheckAppointmentView(LoginMixin, View):
    from student.models import Appointment

    def get(self, request):
        appointments = Appointment.objects.filter(status="ACCEPTED").all()
        ctx = {
            "appointments": appointments,
        }
        return render(request, "student/appointments.html", ctx)
