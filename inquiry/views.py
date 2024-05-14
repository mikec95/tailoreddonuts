from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import InquiryForm


def inquiry_form(request):
    """
    view function for displaying the Inquiry Form
    """
    return render(request, 'inquiry/inquiry-form.html')


def submit_form(request):
    if request.method == 'POST':
        # Process form data here
        # Create a new instance of the InquiryForm model
        form_data = InquiryForm(
            first_name=request.POST.get('first-name'),
            last_name=request.POST.get('last-name'),
            phone_number=request.POST.get('phone-number'),
            email=request.POST.get('email'),
            special_requests=request.POST.get('special-requests')
        )
        form_data.save()

        # Redirect to a success page or another URL
        return render(request, 'inquiry/inquiry-form.html')
