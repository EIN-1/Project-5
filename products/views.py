#/workspace/Project-5/products/views.py
from django.core.paginator import Paginator
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

    paginator = Paginator(products, 10)  # Show 10 courses per page

    # Get the page number from the request
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)  # This gets the current page’s data

    return render(request, 'products/products.html', {'page_obj': page_obj})
    
    # print("products in database =",products)
    # total_products = products.count()  # Count total products
    # context = {
    #     'total_products': total_products,
    #     'products': products,
    # }
    # return render(request, 'home/index.html', context)

def retrieve_product(request, id):
    product = Product.objects.get(id=id)

    return render(request, 'products/product.html')