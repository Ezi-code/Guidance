from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.views.generic import View


class LoginView(View):
    template_name = "login.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            print(user)
            return redirect("core:dashboard")
        else:
            return render(request, self.template_name)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("core:home")
