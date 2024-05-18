from django.shortcuts import render
from .models import GalleryImage
from django.core.paginator import Paginator


def gallery_index(request):
    """
    View function for rendering the gallery page.
    """
    items = GalleryImage.objects.all()  # Query all items from your model
    paginator = Paginator(items, 6)  # Show 9 items per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'items': items, 'page_obj': page_obj}

    # Render the HTML template
    return render(request, 'gallery/gallery.html', context)
