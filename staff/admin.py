from django.contrib import admin
from staff.models import (
    Professional,
    CaseManagementPrgressNotes,
    ClientReferral,
)


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


admin.site.register(Professional, ProfessionalAdmin)
admin.site.register(ClientReferral, ClientReferralAdmin)
admin.site.register(CaseManagementPrgressNotes, CaseManagementPrgressNotesAdmin)
