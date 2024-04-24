from django.contrib import admin
from .models import InquiryForm


class InquiryFormAdmin(admin.ModelAdmin):
    readonly_fields = [
        'first_name',
        'last_name',
        'preferred_contact_time',
        'phone_number',
        'company_name',
        'num_guests',
        'event_type',
        'event_date',
        'pickup_delivery',
        'pickup_name',
        'pickup_date',
        'delivery_date',
        'delivery_address',
        'special_requests',
    ]


admin.site.register(InquiryForm, InquiryFormAdmin)
