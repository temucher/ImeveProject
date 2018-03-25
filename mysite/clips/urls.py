from django.urls import path
from . import views

urlpatterns = [
    path('', views.video_list, name='video_list'),
    path('clips/<int:pk>', views.video_detail, name='video_detail')
]

'''
    path('clips/<int:pk>', views.video_reg, name='video_reg'),
    path('clips/<int:pk>', views.video_360, name='video_360')
    '''