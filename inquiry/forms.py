# forms.py
from django import forms
from .models import InquiryForm


class ContactForm(forms.ModelForm):
    class Meta:
        model = InquiryForm
        fields = ['first_name', 'last_name',
                  'phone_number', 'email',
                  'subject', 'special_requests']
        # Exclude the time_sent field from the form
        exclude = ['time_sent', 'date_sent']
