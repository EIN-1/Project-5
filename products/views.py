#/workspace/Project-5/products/views.py
from django.shortcuts import render
from .models import Product

# Create your views here.
""" A view to all products including sorting and search queries """
def list_all_products(request):
    products = Product.objects.all()

    context = {

    'products': products,
    }

    return render(request, 'products/products.html', context)

