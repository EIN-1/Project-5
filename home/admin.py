from django.contrib import admin
from .models import Carousel

@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ('label', 'active',)
    search_fields = ('label',)
    list_filter = ('label','text',)
    list_editable = ('active',)
    ordering = ('label',)