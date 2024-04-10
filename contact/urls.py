from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    # Inquiry page Url
    path('', views.contact_form, name='contact_url'),
]
