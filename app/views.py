from django.shortcuts import render, get_object_or_404
from .models import crops

def index(request):
    all_crops = crops.objects.all()
    return render(request, 'app/index.html', {'all_crops': all_crops})






