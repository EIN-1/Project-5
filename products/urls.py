from django.urls import path
from . import views
#/workspace/Project-5/products/urls.py
urlpatterns = [
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('<int:id>/', views.retrieve_product, name='product-detail'),
    path('', views.list_all_products, name='products'),
]