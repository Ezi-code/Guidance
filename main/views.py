from django.shortcuts import render
from django.views.generic import View


class AboutView(View):
    def get(self, request):
        return render(request, "main/about.html")
