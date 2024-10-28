from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'id',
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

