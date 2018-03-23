from django.shortcuts import render
from .models import Clip
# Create your views here.

def base(request):
    clips = Clip.objects.order_by('scene')
    return render(request, 'clips/base.html', {'clips': clips})