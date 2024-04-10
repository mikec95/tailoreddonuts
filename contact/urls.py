from django.urls import path
from . import views

urlpatterns = [
    # Inquiry page Url
    path('inquiry/', views.inquiry_form, name='inquiry_url'),
]
