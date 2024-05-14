from django.contrib import admin
from .models import InquiryForm


class InquiryFormAdmin(admin.ModelAdmin):
    readonly_fields = [
        'first_name',
        'last_name',
        'phone_number',
        'email',
        'special_requests',
        'date_time_sent'
    ]


admin.site.register(InquiryForm, InquiryFormAdmin)
