from django.shortcuts import render


def home_index(request):
    """
    View function for rendering the home page.
    """
    # Render the HTML template with the provided context
    return render(request, 'home/home.html')
