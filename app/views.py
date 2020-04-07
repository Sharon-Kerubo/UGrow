from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import crops

class IndexView(generic.ListView):
    model = crops
    template_name = 'app/index.html'

class LocationView(generic.ListView):
    model = crops
    template_name = 'app/location.html'
class LoginView(generic.ListView):
    model = crops
    template_name = 'app/login.html'
class KisiiView(generic.ListView):
    model = crops
    template_name = 'app/kisii.html'
