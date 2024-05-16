from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    # Main Page Url
    path('', views.home_index, name='home')
]
