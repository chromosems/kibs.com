from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('service', views.service, name="service"),
    path('contact', views.contact, name="contact"),
    path('fire', views.fire, name='fire'),
    path('gate', views.gate, name="gate"),
    path('metal', views.metal, name="metal"),
    path('electric', views.electric, name="electric"),
    path('camera', views.camera, name="camera"),
    path('car', views.car, name="car."),
    path('access', views.access, name="access"),
    path('attendance', views.attendance, name="attendance"),
    path('intercom', views.intercom, name="intercom"),
    path('client', views.client, name="client")
]
