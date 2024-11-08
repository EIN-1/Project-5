from django.urls import path
from . import views
#/workspace/Project-5/products/urls.py
urlpatterns = [
    path('<int:id>/', views.retrieve_product, name='product-detail'),
    path('', views.list_all_products, name='products'),
]