#/workspace/Project-5/products/views.py
from django.shortcuts import render
from django.contrib import messages
from django.db.models import Q
from .models import *

# Create your views here.
""" A view to return the index page """
def list_all_products(request):
    products = Product.objects.all()
    total_products = products.count()
context = {
        'total_products': total_products,
        'products': products,}

return render(request, 'home/index.html', context)

