from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.views.generic import View, TemplateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User

# Create your views here.


class LoginView(View):
    template_name = "login.html"
    model = User

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return reverse_lazy(request.path)
        else:
            return redirect("account:login")


class LogoutView(View):
    def get(self, request):
        return reverse_lazy("core:home")


class RegisterView(CreateView): ...
