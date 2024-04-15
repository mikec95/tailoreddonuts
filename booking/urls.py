from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    # Inquiry page Url
    path('', views.booking_form, name='booking_url'),
]
