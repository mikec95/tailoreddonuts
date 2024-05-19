from django.shortcuts import render

# Create your views here.


def locator_index(request):
    """
    view function for displaying the Locator page
    """
    return render(request, 'locator/locator.html')
