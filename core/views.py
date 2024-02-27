from django.shortcuts import render, redirect
from django.views.generic import (
    View,
    CreateView,
    ListView,
    DeleteView,
    UpdateView,
    TemplateView,
)
from django.urls import reverse_lazy
from core.models import Guidance
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

# from django.contrib.auth.mixin import LoginRequiredMixin
from django.core.mail import EmailMessage
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = "index.html"
    # def get(self, request):
    #     return render(request, "index.html")


class BookView(LoginRequiredMixin, CreateView):
    template_name = "book.html"
    success_url = reverse_lazy("core:notitfications")
    login_required = True
    model = Guidance
    fields = "__all__"

    # def get(self, request):
    #     if request.user.is_authenticated:
    #         return render(request, "book.html")
    #     else:
    #         return redirect("core:login")

    # def post(self, request):
    #     name = request.POST.get("name")
    #     email = request.POST.get("email")
    #     phone = request.POST.get("phone")
    #     level = request.POST.get("level")
    #     department = request.POST.get("department")
    #     service = request.POST.get("service")
    #     reason = request.POST.get("reason")
    #     if service == "guidance":
    #         appointment = Guidance.objects.create(
    #             fname=name,
    #             email=email,
    #             phone=phone,
    #             level=level,
    #             service_type=service,
    #             department=department,
    #             reason=reason,
    #         )
    #         appointment.clean_fields()
    #         appointment.save()
    #     return redirect("core:home")


class DashboardView(ListView):
    queryset = Guidance.objects.all()
    success_url = "core:appointment"

    # def get(self, request):
    #     if request.user.is_authenticated:
    #         return redirect("core:appointment")
    #     else:
    #         return redirect("core:login")


class NotificationsView(View):
    def get(self, request):
        return render(request, "notifications.html")


class CheckAppointmentView(View):
    from core.models import Guidance

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, "appointments.html")
        else:
            return redirect("core:login")
