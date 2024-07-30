from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User

from stroller.models import Stroller


def index(request):
    featured_strollers = Stroller.objects.filter(is_featured=True)
    context = {
        'featured_strollers': featured_strollers,
    }
    return render(request=request, template_name='pages/index.html', context=context)


def about(request):
    return render(request=request, template_name='pages/about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')

        email_subject = f"Нова заявка:"
        message_body = (f"Імя: {name} \n"
                        f"Email: {email} \n"
                        f"Телефон: {phone} \n"
                        f"Повідомлення: {message}")

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email

        send_mail(
            email_subject,
            message_body,
            "vatikan98@gmail.com",
            [admin_email],
            fail_silently=False,
        )
        messages.success(request, 'Your message has been sent successfully.')
        return redirect('pages:contacts')

    return render(request, 'pages/contact.html')

