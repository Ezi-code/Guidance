from django.contrib import admin
from staff.models import (
    Session,
    Professional,
    CaseManagementPrgressNotes,
    ClientReferral,
)


class SessionAdmin(admin.ModelAdmin):
    list_display = ["student", "date"]
    list_filter = ["date"]
    search_fields = ["student", "date"]


class ProfessionalAdmin(admin.ModelAdmin):
    list_display = ["name", "service_type", "is_available"]
    list_filter = ["service_type", "is_available"]
    search_fields = ["name", "email", "phone", "service_type"]


class CaseManagementPrgressNotesAdmin(admin.ModelAdmin):
    list_display = ["client"]
    list_filter = ["client"]
    search_fields = ["client"]


class ClientReferralAdmin(admin.ModelAdmin):
    list_display = ["name", "referred_by", "reason"]
    list_filter = ["name", "referred_by", "counsellor_id"]
    search_fields = ["name", "referred_by", "counsellor_id"]


admin.site.register(Session, SessionAdmin)
admin.site.register(Professional, ProfessionalAdmin)
admin.site.register(ClientReferral, ClientReferralAdmin)
admin.site.register(CaseManagementPrgressNotes, CaseManagementPrgressNotesAdmin)
