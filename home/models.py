from django.db import models

class Carousel(models.Model):
    imageUrl = models.URLField()
    label = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    active = models.BooleanField(default=False)