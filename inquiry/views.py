from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from .models import InquiryForm
from django.urls import reverse


def inquiry_form(request):
    """
    View function for displaying the Inquiry Form.
    """
    return render(request, 'inquiry/inquiry-form.html')


def submit_form(request):
    if request.method == 'POST':
        try:
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

            # Add a success message
            messages.success(
                request, 'Thank you! We will be in touch with you soon!')

            # Redirect to the same page after form submission
            return HttpResponseRedirect(reverse('inquiry:inquiry_url'))
        except Exception as e:
            # Handle any exceptions here
            messages.error(request, f'Whoops! An error occurred: {e}')

    # Render the form page for GET requests or if form submission fails
    return render(request, 'inquiry/inquiry-form.html')
