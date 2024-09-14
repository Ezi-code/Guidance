from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.views.generic import View
from django.contrib import messages
from staff.services import LoginMixin
from django.contrib.auth import get_user_model


class StudentRegisterView(View):

    def get(self, request):
        return render(request, "accounts/student_signup.html")
    
    def post(self, request):
        try:
            index_number = request.POST.get("index_number")
            username = request.POST.get("username")
            password = request.POST.get("password")
            password1 = request.POST.get("password1")
            if password != password1:
                messages.error(request, "Passwords do not match")
                return redirect("accounts:student_signup")
            get_user_model().objects.create(index_number=index_number, username=username,password=password, is_student=True)
            messages.success(request, "You are now registered")
            return redirect("accounts:student_login")
        except Exception as e:
            messages.error(request, f"Error: {str(e)}")
            return redirect("accounts:student_signup")


class StudentLoginView(View):
    template_name = "accounts/student_signin.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        try:
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=username, password=password)
        except Exception as e:
            messages.error(request, "Invalid credentials")
            return render(request, self.template_name)
        if user is not None:
            if user.is_student:
                login(request, user)
                messages.success(request, "You are now logged in")
                return redirect("student:requests")
            else:
                messages.error(request, "You are not allowed to login here")
                return redirect("accounts:student_login")
        else:
            messages.error(request, "Invalid credentials")
            return render(request, self.template_name)


class StudentLogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "You are now logged out")
        return redirect("student:home")


class StaffLoginView(View):
    def get(self, request):
        return render(request, "accounts/staff_signin.html")

    def post(self, request):
        try:
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
        except Exception as e:
            messages.error(request, "Invalid credentials")
            return redirect("accounts:staff_login")
        if user is not None:
            if user.is_staff:
                login(request, user)
                messages.success(request, "You are now logged in")
                return redirect("staff:home")
            else:
                messages.error(request, "You are not allowed to login here")
                return redirect("accounts:staff_login")
        messages.error(request, "Invalid credentials")
        return redirect("accounts:staff_login")


class LogoutView(LoginMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, "You are now logged out")
        return redirect("main:homepage")


def student_check_username(request):
    username = request.POST.get("username")
    if get_user_model().objects.filter(index_number=username, is_student=True).exists():
        return HttpResponse("<span style='color:green'>User ID is valid</span>")
    return HttpResponse("<span style='color:red'>User ID does not exist</span>")


def staff_check_username(request):
    username = request.POST.get("username")
    if get_user_model().objects.filter(index_number=username, is_staff=True).exists():
        return HttpResponse("<span style='color:green'>User ID is valid</span>")
    return HttpResponse("<span style='color:red'>User ID does not exist</span>")
