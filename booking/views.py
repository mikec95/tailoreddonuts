from django.shortcuts import render


def booking_form(request):
    """
    view function for displaying the Booking Form
    """
    return render(request, 'booking/booking-form.html')
