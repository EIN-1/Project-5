#/workspace/Project-5/products/models.py
from django.db import models

# Create your models here.
class Product(models.Model):
   
    product = models.IntegerField('product', null=True, blank=True)
    id = models.IntegerField(primary_key=True, unique=True)
    courseName = models.CharField(max_length=254)
    instructor = models.CharField(max_length=254)
    courseUrl = models.URLField(max_length=1024, null=True, blank=True)
    imageUrl = models.URLField(max_length=1024, null=True, blank=True)
    description = models.TextField()
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    reviews = models.IntegerField(null=True, blank=True)
    duration = models.DecimalField(max_digits=6, decimal_places=2)
    lectures = models.IntegerField(null=True, blank=True)
    level = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    flag = models.BooleanField(default=False)
    students = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.courseName