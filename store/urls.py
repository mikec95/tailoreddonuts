from django.urls import path
from . import views

urlpatterns = [
    # Main Page Url
    path('', views.store_index, name='store'),

    # Inquiry page Url
    path('inquiry/', views.inquiry_form, name='inquiry_url'),

    # Individual Product Url
    path('product/<slug:product_slug>',
         views.product_info, name='product-info'),

    # Individual Category Url
    path('category/<slug:category_slug>',
         views.list_category, name="list-category")
]
