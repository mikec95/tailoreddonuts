from django.contrib import admin
from .models import InquiryForm


class InquiryFormAdmin(admin.ModelAdmin):
    readonly_fields = [
        'first_name',
        'last_name',
        'phone_number',
        'email',
        'subject',
        'special_requests',
        'date_time_sent'
    ]
    list_display = ('first_name',
                    'last_name',
                    'phone_number',
                    'email',
                    'subject',
                    'special_requests',
                    'date_time_sent')
    list_filter = ('first_name',
                   'last_name',
                   'phone_number',
                   'email',
                   'subject',
                   'special_requests',
                   'date_time_sent')
    search_fields = ('first_name',
                     'last_name',
                     'phone_number',
                     'email',
                     'subject',
                     'special_requests',
                     'date_time_sent')


admin.site.register(InquiryForm, InquiryFormAdmin)
