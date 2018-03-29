from django.db import models

# Create your models here.
class Clip(models.Model):
    file_path = models.CharField(max_length=50, default='clips/videos/mayo.mp4')
    thumb_path = models.CharField(max_length=50, default='clips/images/mayo.png')
    scene = models.CharField(max_length=10)
    take = models.CharField(max_length=10)
    starRating = models.IntegerField() # potentially make this an IntegerField and map that to star count
    is360video = models.BooleanField(default=False)

def __str__(self):
    return self.scene