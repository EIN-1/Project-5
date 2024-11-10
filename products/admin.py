from django.contrib import admin
from .models import Product, Category
#/workspace/Project-5/products/admin.py
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (        
        'courseName',
        'rating',
        'lectures',
        'level',
        'price',
        'flag',
        'category',
    )

    list_editable = ('category',)

    ordering = ('id',)
admin.site.register(Product, ProductAdmin)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    list_filter = ('name',)

    # You can customize the display here if needed
    ordering = ('name',)

