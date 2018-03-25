from django.shortcuts import render, get_object_or_404
from .models import Clip
# Create your views here.

''' Not sure if needed
def base(request):
    clips = Clip.objects.order_by('scene')
    return render(request, 'clips/base.html', {'clips': clips})
'''


def video_list(request):
    clips = Clip.objects.order_by('scene')
    return render(request, 'clips/video_list.html', {'clips': clips})

'''
def video_360(request, pk):
    clip = get_object_or_404(Clip, pk=pk)
    return render(request, 'clips/video_360.html', {'clip': clip})


def video_reg(request, pk):
    clip = get_object_or_404(Clip, pk=pk)
    return render(request, 'clips/video_reg.html', {'clip': clip})
'''

def video_detail(request, pk):
    clip = get_object_or_404(Clip, pk=pk)
    if (clip.is360video):
        return render(request, 'clips/video_360.html', {'clip': clip})
    else:
        return render(request, 'clips/video_reg.html', {'clip': clip})
