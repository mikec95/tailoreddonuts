from django.db import models
from django.db import models


from django.db import models


class InquiryForm(models.Model):
    CONTACT_TIMES = [
        ('morning', 'Morning'),
        ('afternoon', 'Afternoon'),
        ('evening', 'Evening'),
    ]
    EVENT_TYPES = [
        ('wedding', 'Wedding'),
        ('gathering', 'Large Gathering'),
        ('birthday', 'Birthday'),
        ('corp-event', 'Corporate Event'),
        ('popup', 'Popup'),
    ]
    PICKUP_DELIVERY_CHOICES = [
        ('pickup', 'Pickup'),
        ('delivery', 'Delivery'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    preferred_contact_time = models.CharField(
        max_length=20, choices=CONTACT_TIMES)
    phone_number = models.CharField(max_length=20)
    company_name = models.CharField(max_length=100)
    num_guests = models.IntegerField()
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES)
    event_date = models.DateField()
    pickup_delivery = models.CharField(
        max_length=10, choices=PICKUP_DELIVERY_CHOICES)
    pickup_name = models.CharField(max_length=100, blank=True, null=True)
    pickup_date = models.DateField(blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)
    delivery_address = models.CharField(max_length=200, blank=True, null=True)
    special_requests = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Inquiry - {self.first_name} {self.last_name}"
