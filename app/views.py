from django.shortcuts import render, get_object_or_404, redirect
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Counties, Soils, SoilPH, crop

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
def county_datasets(request):
    counties = serialize('geojson', Counties.objects.all())
    return HttpResponse(counties, content_type='json')
def soils_datasets(request):
    soils = serialize('geojson', Soils.objects.all())
    return HttpResponse(soils, content_type='json')
def soilph_datasets(request):
    soilph = serialize('geojson', SoilPH.objects.all())
    return HttpResponse(soilph, content_type='json')
def crop_datasets(request):
    crops = serialize('geojson', crop.objects.all())
    return HttpResponse(crops, content_type='json')
