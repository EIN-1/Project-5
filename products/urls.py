from django.urls import path
from . import views
#/workspace/Project-5/products/urls.py
urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('confirm-order/', views.order_confirmation, name='order_confirmation'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('<int:id>/', views.retrieve_product, name='product-detail'),
    path('', views.list_all_products, name='products'),
]