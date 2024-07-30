from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User

from .models import Contact


def inquiry_short(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        phone = request.POST['phone']
        message = request.POST['message']

        contact = Contact(
            first_name=first_name,
            phone=phone,
            message=message)

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
            "New Car Inquiry",
            f"You have a new inquiry for the car",
            "vatikan98@gmail.com",
            [admin_email],
            fail_silently=False,
        )

        contact.save()
        messages.success(request, 'Your message has been sent.')
        return redirect('home')
