from django.shortcuts import render
from .models import Clip
# Create your views here.

def base(request):
    return render(request, 'clips/base.html', context=None)