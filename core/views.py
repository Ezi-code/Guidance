from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View, CreateView
from django.urls import reverse_lazy
from core.models import Guidance
from django.core.mail import EmailMessage
from django.views.generic.base import TemplateView
from core.services import LoginMixin


class HomeView(TemplateView):
    template_name = "index.html"


class BookView(LoginMixin, CreateView):
    template_name = "book.html"
    success_url = reverse_lazy("core:notitfications")
    login_required = True
    model = Guidance
    fields = "__all__"


class DashboardView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("core:appointment")
        else:
            return redirect("core:login")


class NotificationsView(View):
    def get(self, request):
        return render(request, "notifications.html")


class CheckAppointmentView(View):
    from core.models import Guidance

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, "appointments.html")
        else:
            return redirect("accounts:login")
