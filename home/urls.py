from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    # Main Page Url
    path('', views.home_index, name='home'),

    # Individual Product Url
    path('product/<slug:product_slug>',
         views.product_info, name='product-info'),

    # Individual Category Url
    path('category/<slug:category_slug>',
         views.list_category, name="list-category")
]
