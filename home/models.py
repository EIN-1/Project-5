from django.db import models

# Create your models here.
class Carousel(models.Model):
    imageUrl = models.URLField()
    label = models.CharField(max_length=255)
    text = models.CharField(max_length=255)