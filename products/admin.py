from django.contrib import admin
from .models import Product
#/workspace/Project-5/products/admin.py
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        
        'courseName',
        'instructor',
        'courseUrl',
        'imageUrl',
        'description',
        'rating',
        'reviews',
        'duration',
        'lectures',
        'level',
        'price',
        'flag',
        'students'
    )

    ordering = ('id',)
admin.site.register(Product, ProductAdmin)


