from django.db import models

# Create your models here.
class Clip(models.Model):
    file_path = models.CharField(max_length=50, default='static/videos/darude.mp4')
    scene = models.CharField(max_length=10)
    take = models.CharField(max_length=10)
    starRating = models.CharField(max_length=10) # potentially make this an IntegerField and map that to star count

def __str__(self):
    return self.scene