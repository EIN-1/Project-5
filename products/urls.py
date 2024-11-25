from django.urls import path
from . import views
#/workspace/Project-5/products/urls.py
urlpatterns = [    
    path('orders/', views.all_orders, name="admin_orders"),
    path('orders/edit/<int:order_id>/', views.edit_order, name="admin_edit_order"),
    path('orders/<int:order_id>/', views.order_detail, name="admin_order"),
    path('edit/<int:course_id>/', views.edit_course, name='edit_course'),
    path('delete/<int:course_id>/', views.delete_course, name='delete_course'),
    path('create/', views.create_course, name='create_course'),
    path('complete-payment/', views.complete_payment, name='complete_payment'),
    path('my-orders/', views.my_orders, name='my_orders'),
    path('my-orders/<int:order_id>', views.order_details, name='order_details'),
    path('checkout/', views.checkout, name='checkout'),
    path('confirm-order/', views.order_confirmation, name='order_confirmation'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('add-review/<int:product_id>/', views.add_review, name='add-review'),
    path('delete_course/<int:course_id>/', views.delete_course, name='admin_delete_course'),
    path('<int:id>/', views.retrieve_product, name='product-detail'),
    path('', views.list_all_products, name='products'),
]