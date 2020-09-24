from django.core.mail import send_mail
from django.shortcuts import render, redirect

from Form_django.settings import EMAIL_HOST_USER
from .forms import Peopleform


def register(request):
    if request.method == 'POST':
        form = Peopleform(request.POST)
        if form.is_valid():
            form.save()
            subject = 'Thank you for registering'
            message = 'Hope you are enjoying the service offer by forms'
            recepient = str(form['email'].value())
            send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently=False)
            return redirect('/success/')
    else:
        form = Peopleform()
    context = {'form': form}
    return render(request, 'Register-pages/index.html', context)


def success(request):
    return render(request, 'Register-pages/success.html')


