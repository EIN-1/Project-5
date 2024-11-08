#/workspace/Project-5/products/views.py
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart
from django.shortcuts import redirect, get_object_or_404

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

    return render(request, 'products/product.html', {'product':product})


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.user.is_authenticated:
        # For logged-in users: add to Cart model in the database
        cart, created = Cart.objects.get_or_create(user=request.user, product=product)
    else:
        # For anonymous users: store cart items in the session
        cart = request.session.get('cart', [])
        if product_id in cart:
            return
        else:
            cart.append(product_id)
        request.session['cart'] = cart  # Save cart back to session

    return redirect('cart_detail')  # Redirect to cart detail page or any page of your choice

def cart_detail(request):
    if request.user.is_authenticated:
        # Retrieve cart from database for logged-in users
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        # Retrieve cart from session for anonymous users
        cart = request.session.get('cart', [])
        for product_id in cart:
            product = get_object_or_404(Product, id=product_id)
            cart.append(product)

    return render(request, 'cart/details.html', {'cart_items': cart})