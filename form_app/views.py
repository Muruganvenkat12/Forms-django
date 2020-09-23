from django.core.mail import send_mail
from django.shortcuts import render

from Form_django.settings import EMAIL_HOST_USER
from .forms import Peopleform


def register(request):
    form = Peopleform()
    if request.method == 'POST':
        form = Peopleform(request.POST)
        if form.is_valid():
            form.save()
        subject = 'Thank you for registering'
        message = 'Hope you are enjoying the mailing service offer by forms'
        recepient = str(form['email'].value())
        send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently=False)
    context = {'form': form}
    return render(request, 'Register-pages/index.html', context)
