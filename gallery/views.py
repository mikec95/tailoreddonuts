from django.shortcuts import render


def gallery_index(request):
    """
    View function for rendering the gallery page.
    """
    # Render the HTML template
    return render(request, 'gallery/gallery.html')
