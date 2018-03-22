from django.db import models

# Create your models here.
class Clip(models.Model):
    scene = models.CharField(max_length=10)
    take = models.CharField(max_length=10)
    starRating = models.CharField(max_length=10)

def __str__(self):
    return self.scene