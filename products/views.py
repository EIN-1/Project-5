#/workspace/Project-5/products/views.py
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart, CartItem
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
        # For logged-in users, add to the Cart model in the database
        cart, created = Cart.objects.get_or_create(user=request.user)
        # Check if the product is already in the cart
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    else:
        # For anonymous users, store cart items in the session
        cart = request.session.get('cart', set())
        cart = set(cart)  # Convert to set for unique items
        cart.add(product_id)  # Add the product ID if not already present
        request.session['cart'] = list(cart)  # Save the cart back to session

    return redirect('cart_detail')  # Redirect to the cart detail page or any page of your choice

def cart_detail(request):
    if request.user.is_authenticated:
        # Retrieve cart items from the database for logged-in users
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = cart.items.all()
    else:
        # Retrieve cart items from the session for anonymous users
        cart_ids = request.session.get('cart', [])
        cart_items = [get_object_or_404(Product, id=product_id) for product_id in cart_ids]

    return render(request, 'cart/details.html', {'cart_items': cart_items})