from django.db import models
from django.utils import timezone


class InquiryForm(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20, default='N/A')
    email = models.EmailField(max_length=255, default='example@example.com')
    special_requests = models.TextField(blank=True, null=True)
    date_time_sent = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Inquiry - {self.first_name} - {self.last_name} - {self.date_time_sent}"
