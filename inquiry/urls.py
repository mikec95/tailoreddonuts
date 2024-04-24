from django.urls import path
from . import views

app_name = 'inquiry'

urlpatterns = [
    # Inquiry page Url
    path('', views.inquiry_form, name='inquiry_url'),
    path('submit-inquiry', views.submit_form, name="submit_inquiry_url")
]
