from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View, CreateView
from django.urls import reverse_lazy
from core.models import Appointment, Notifications, Professional
from django.views.generic.base import TemplateView
from core.services import LoginMixin


class HomeView(TemplateView):
    template_name = "index.html"


class BookView(LoginMixin, CreateView):
    template_name = "book.html"
    success_url = reverse_lazy(
        "core:notitfications",
        kwargs={
            "message": "Appointment booked successfully",
        },
    )
    login_required = True
    model = Appointment
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["professionals"] = Professional.objects.all()
        return context


class DashboardView(LoginMixin, View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("core:appointment")
        else:
            return redirect("core:login")


class NotificationsView(LoginMixin, View):
    def get(self, request):
        notifications = Notifications.objects.filter(user=request.user).all()
        ctx = {
            "notifications": notifications,
        }
        return render(request, "notifications.html", ctx)


class CheckAppointmentView(LoginMixin, View):
    from core.models import Appointment

    def get(self, request):
        appointments = Appointment.objects.filter(status="ACCEPTED").all()
        ctx = {
            "appointments": appointments,
        }
        return render(request, "appointments.html", ctx)
