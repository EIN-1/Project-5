from django.shortcuts import render
from products.models import Product

# Create your views here.

def index(request):
    """ A view to return the index page """
    products = Product.objects.all()  # Fetch all products
    print("products in database =",products)
    total_products = products.count()  # Count total products
    context = {
        'total_products': total_products,
        'products': products,
    }

    return render(request, 'home/index.html',context)
