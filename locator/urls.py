from django.urls import path
from . import views

app_name = 'locator'

urlpatterns = [
    # Menu Page Url
    path('', views.locator_index, name='locator_url'),
]
