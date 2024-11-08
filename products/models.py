#/workspace/Project-5/products/models.py
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()

class Product(models.Model):    
class Product(models.Model):    
    courseName = models.CharField(max_length=254)
    instructor = models.CharField(max_length=254)
    courseUrl = models.URLField(max_length=1024, null=True, blank=True)
    imageUrl = models.URLField(max_length=1024, null=True, blank=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)
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