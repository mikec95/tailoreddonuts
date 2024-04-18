from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    # Menu Page Url
    path('', views.menu_index, name='menu_url'),
]
