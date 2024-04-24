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
            preferred_contact_time=request.POST.get('best-time'),
            phone_number=request.POST.get('contact'),
            company_name=request.POST.get('company-name'),
            num_guests=request.POST.get('quantity'),
            event_type=request.POST.get('event-type'),
            event_date=request.POST.get('event-date'),
            pickup_delivery=request.POST.get('pickup-delivery'),
            pickup_name=request.POST.get('pickup-name'),
            pickup_date=request.POST.get('pickup-date'),
            delivery_date=request.POST.get('delivery-date'),
            delivery_address=request.POST.get('delivery-address'),
            special_requests=request.POST.get('special-requests')
        )
        form_data.save()

        # Redirect to a success page or another URL
        return render(request, 'home/home.html')
