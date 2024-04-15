from django.urls import path
from . import views

app_name = 'inquiry'

urlpatterns = [
    # Inquiry page Url
    path('', views.inquiry_form, name='inquiry_url'),
]
