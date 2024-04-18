from django.shortcuts import render

# Create your views here.


def menu_index(request):
    """
    view function for displaying the Menu
    """
    return render(request, 'menu/menu.html')
