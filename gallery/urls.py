from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    # Gallery page Url
    path('', views.gallery_index, name='gallery_url'),
]
