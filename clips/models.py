from django.db import models

# Create your models here.
class Clip(models.Model):
    file_path = models.FilePathField(path="clips/static/clips/videos", allow_files=True)
    thumb_path = models.FilePathField(path="clips/static/clips/images", allow_files=True)
    scene = models.CharField(max_length=10)
    take = models.CharField(max_length=10)
    starRating = models.IntegerField() # potentially make this an IntegerField and map that to star count
    is360video = models.BooleanField(default=False)

def __str__(self):
    return self.scene