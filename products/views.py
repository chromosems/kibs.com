from django.shortcuts import render
from django.core.mail import send_mail


def home(request):
    return render(request, 'home.html', {})


def about(request):
    return render(request, 'about.html', {})


def service(request):
    return render(request, 'service.html', {})


def contact(request):
    if request.method == "POST":
        names = request.POST['names']
        from_email = request.POST['from-email']
        subject = request.POST['subject']
        message = request.POST['message']

        # send an email

        send_mail(subject, message, from_email, ['kibussystemltd@gmail.com'])

        return render(request, 'contact.html', {'names': names})
    else:
        return render(request, 'contact.html', {})


def fire(request):
    return render(request, 'fire.html', {})


def gate(request):
    return render(request, 'gate.html', {})


def metal(request):
    return render(request, 'metal.html', {})


def electric(request):
    return render(request, 'electric.html', {})


def camera(request):
    return render(request, 'camera.html', {})


def car(request):
    return render(request, 'car.html', {})


def access(request):
    return render(request, 'access.html', {})


def attendance(request):
    return render(request, 'attendance.html', {})


def intercom(request):
    return render(request, 'intercom.html', {})


def client(request):
    return render(request, 'client.html', {})
