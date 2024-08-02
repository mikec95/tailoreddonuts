from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from .models import InquiryForm
from django.urls import reverse
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


def inquiry_form(request):
    """
    View function for displaying the Inquiry Form.
    """
    return render(request, 'inquiry/inquiry-form.html')


def submit_form(request):
    if request.method == 'POST':
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        phone_number = request.POST.get('phone-number')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        special_requests = request.POST.get('special-requests')

        # Collect form data
        form_data = InquiryForm(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            email=email,
            subject=subject,
            special_requests=special_requests
        )

        try:
            # Save the form data
            form_data.save()

            # Send confirmation email
            send_confirmation_email(f"{first_name} {last_name}", email)

            # Send notification email to Administrator
            send_notification_email(first_name=first_name, last_name=last_name,
                                    user_email=email, subject=subject, special_requests=special_requests)

            # Add a success message
            messages.success(
                request, f'Thank you for your message! Please check your email  {email} for a confirmation.')

            # Redirect to the inquiry form page
            return HttpResponseRedirect(reverse('inquiry:inquiry_url'))
        except Exception as e:
            # Handle exceptions and show an error message
            messages.error(request, f'Whoops! An error occurred {e}')

    # Render the form page for GET requests or if form submission fails
    return render(request, 'inquiry/inquiry-form.html')


def send_confirmation_email(user_name, user_email):
    """
    Send a confirmation email to the user.
    """
    subject = 'Tailored Donuts Request Confirmation'
    from_email = 'mikecarbonari1@gmail.com'
    context = {'user_name': user_name}
    message = render_to_string('inquiry/email_confirmation.html', context)

    email = EmailMessage(subject, message, from_email, [user_email])
    email.content_subtype = 'html'
    email.send(fail_silently=False)


def send_notification_email(first_name, last_name, user_email, subject, special_requests):
    """
    Send a notification email to the administrator.
    """
    email_subject = f'You have a new {subject} Message'
    from_email = 'mikecarbonari1@gmail.com'
    context = {
        'first_name': first_name,
        'last_name': last_name,
        'user_email': user_email,
        'subject': subject,
        'special_requests': special_requests
    }
    message = render_to_string('inquiry/email_notification.html', context)

    email = EmailMessage(email_subject, message, from_email, [
                         "tailoreddonuts@gmail.com"])
    email.content_subtype = 'html'
    email.send(fail_silently=False)
