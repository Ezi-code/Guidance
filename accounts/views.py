from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.views.generic import View, TemplateView, CreateView
from django.urls import reverse_lazy
from accounts.models import User
from forms.accounts.forms import RegisterForm

# Create your views here.


class LoginView(View):
    template_name = "login.html"
    # model = User

    def get(self, request):
        return render(request, self.template_name)

    # def get(self, request):
    #     return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            print(user)
            return reverse_lazy("core:dashboard")
        else:
            return render(request, self.template_name)


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "register.html", {form: "form"})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return


# class RegisterView(CreateView):
#     form_class = RegisterForm
#     template_name = "register.html"
#     model = User
#     fields = ["username", "email", "password"]
#     queryset = User.objects.all()


class LogoutView(View):
    def get(self, request):
        logout(request)
        return reverse_lazy("core:home")


# class RegisterView(CreateView): ...
