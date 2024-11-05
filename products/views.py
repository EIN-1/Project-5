#/workspace/Project-5/products/views.py
from django.shortcuts import render
from .models import Product

# Create your views here.
""" A view to all products including sorting and search queries """
# def list_all_products(request):
#     products = Product.objects.all()

#     print("products in database =",products)
   
#     return render(request, 'products/products.html', {'products': products})


def list_all_products(request):
    products = Product.objects.all()  # Fetch all products
    print("products in database =",products)
    total_products = products.count()  # Count total products
    context = {
        'total_products': total_products,
        'products': products,
    }
    return render(request, 'home/index.html', context)

