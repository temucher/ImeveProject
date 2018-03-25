from django.shortcuts import render, get_object_or_404, redirect
from .models import Clip
# Create your views here.


def video_list(request):
    clips = Clip.objects.order_by('scene')
    return render(request, 'clips/video_list.html', {'clips': clips})


def video_detail(request, pk):
    clip = get_object_or_404(Clip, pk=pk)
    if (clip.is360video):
        return render(request, 'clips/video_360.html', {'clip': clip})
    else:
        return render(request, 'clips/video_reg.html', {'clip': clip})


def video_delete(request, pk):
    clip = get_object_or_404(Clip, pk=pk)
    clip.delete()
    return redirect('video_list')

