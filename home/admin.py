from django.contrib import admin
from .models import Carousel

# Register your models here.
@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ('label', 'active',)
    search_fields = ('label',)
    list_filter = ('label','text',)
    list_editable = ('active',)

    # You can customize the display here if needed
    ordering = ('label',)