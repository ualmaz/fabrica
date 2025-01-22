from django.shortcuts import render
from django.utils.translation import gettext as _
from .models import Client
from .forms import ContactForm
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def portfolio(request):
  return render(request, 'portfolio.html')

def mens(request):
  return render(request, 'mens.html')

def womens(request):
  return render(request, 'womens.html')

def kids(request):
  return render(request, 'kids.html')

def sport(request):
  return render(request, 'sport.html')

def uniform(request):
  return render(request, 'uniform.html')

def bed(request):
  return render(request, 'bed.html')

def contact(request):
    return render(request, 'contact.html')

def cookies(request):
    return render(request, 'cookie-policy.html')


def contact_view(request):
    print("Contact view reached")
    form = ContactForm()

    if request.method == 'POST':
        print("POST request received")
        form = ContactForm(request.POST)
        if form.is_valid():
            print("Form is valid")

            # Save the form data to the database
            submission = form.save()
            print(f"Saved submission: {submission}")
            # Send an email
            subject = f"New Contact Form Submission from {submission.firstname} {submission.lastname}"
            message = f"""
            You have a new contact form submission:

            Name: {submission.firstname} {submission.lastname}
            Email: {submission.email}
            Phone: {submission.phone}
            Message: {submission.message}

            """
            recipient_email = "ualmaz@gmail.com"
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,  # Your sender email from settings
                [recipient_email],
                fail_silently=False,
            )

            # Add a success message
            messages.success(request, _('Your message has been sent successfully!'))

        else:
            # Add an error message if the form is invalid
            messages.error(request, _('A user with this email alrady exists.'))

    return render(request, 'contact.html', {'form': form})