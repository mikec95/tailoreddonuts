from django.shortcuts import render

from home.models import Product

# Create your views here.


def gallery_index(request):
    """
    View function for rendering the gallery page.
    """
    # Retrieve all products from the database
    all_products = Product.objects.all()
    # Define the context to be passed to the template
    context = {'all_products': all_products}
    # Render the HTML template with the provided context
    return render(request, 'gallery/gallery.html', context=context)
