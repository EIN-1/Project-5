from django.urls import path
from . import views
#/workspace/Project-5/products/urls.py
urlpatterns = [
    path('', views.list_all_products, name='products'),
]