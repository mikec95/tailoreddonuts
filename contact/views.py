from django.shortcuts import render


def inquiry_form(request):
    """
    view function for displaying the Inquiry Form
    """
    return render(request, 'contact/inquiry-form.html')
