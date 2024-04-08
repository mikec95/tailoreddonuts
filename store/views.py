from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def store_index(request):
    """
    View function for rendering the store index page.
    """
    # Retrieve all products from the database
    all_products = Product.objects.all()
    # Define the context to be passed to the template
    context = {'all_products': all_products}
    # Render the HTML template with the provided context
    return render(request, 'store/store.html', context=context)


def categories(request):
    """
    View function for retrieving all categories.
    """
    # Retrieve all categories from the database
    all_categories = Category.objects.all()
    # Return the categories as a dictionary
    return {'all_categories': all_categories}


def list_category(request, category_slug):
    """
    View function for listing products within a specific category.
    """
    # Retrieve the category object based on the slug
    category = get_object_or_404(Category, slug=category_slug)
    # Filter products based on the selected category
    products = Product.objects.filter(category=category)
    # Render the HTML template with the category and products context
    return render(request, 'store/list-category.html', {'category': category, 'products': products})


def product_info(request, product_slug):
    """
    View function for displaying details of a specific product.
    """
    # Retrieve the product object based on the slug
    product = get_object_or_404(Product, slug=product_slug)
    # Define the context to be passed to the template
    context = {'product': product}
    # Render the HTML template with the provided context
    return render(request, 'store/product-info.html', context=context)
