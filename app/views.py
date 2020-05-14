from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import crops, signup

def index(request):
    return render(request, 'app/index.html')
def kisii(request):
    return render(request, 'app/kisii.html')
def kisumu(request):
    return render(request, 'app/kisumu.html')
def eldoret(request):
    return render(request, 'app/eldoret.html')
def meru(request):
    return render(request, 'app/meru.html')
def kiambu(request):
    return render(request, 'app/kiambu.html')
def signup(request):
    return render(request, 'app/signup.html')
def login(request):
    return render(request, 'app/login.html')