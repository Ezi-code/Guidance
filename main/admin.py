from django.contrib import admin
from main.models import Team


class AdminTeam(admin.ModelAdmin):
    list_display = ["name", "email", "phone", "position"]
    search_fields = ["name", "email", "phone", "position"]


admin.site.register(Team, AdminTeam)
