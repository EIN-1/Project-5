from django.contrib import admin
from .models import Product, Category, Order, OrderItems
#/workspace/Project-5/products/admin.py
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (        
        'courseName',
        'rating',
        'instructor',
        'level',
        'price',
        'flag',
        'category',
    )
    list_editable = ('category',)
    list_filter = ('category','rating', 'level', 'flag',)
    search_fields = ('courseName', 'instructor', 'price',)

    ordering = ('id',)
admin.site.register(Product, ProductAdmin)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    list_filter = ('name',)

    # You can customize the display here if needed
    ordering = ('name',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'status', 'stripe_id', 'date',)
    search_fields = ('user',)
    list_filter = ('status','date',)

    # You can customize the display here if needed
    ordering = ('date',)

