from django.shortcuts import render, redirect
from django.views.generic import View
from core.models import Guidance
from django.contrib.auth import authenticate, login, logout


class HomeView(View):
    def get(self, request):
        return render(request, "index.html")


class BookView(View):

    def get(self, request):
        return render(request, "book.html")

    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        level = request.POST.get("level")
        department = request.POST.get("department")
        service = request.POST.get("service")
        reason = request.POST.get("reason")
        if service == "guidance":
            appointment = Guidance.objects.create(
                fname=name,
                email=email,
                phone=phone,
                level=level,
                service_type=service,
                department=department,
                reason=reason,
            )
            appointment.clean_fields()
            appointment.save()
        return redirect("core:home")


class LoginView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
            print(user)
            login(request, user)
            return redirect("home")
        else:
            error_msg = "Invalid username or password"
            print(error_msg)
            return render(request, "login.html")


class DashboardView(View):
    def get(self, request):
        return render(request, "dashboard.html")


class LogoutView(View):
    def get(self, request):
        user = request.user
        print(user)
        logout(request.user)
        return redirect("home")
