#/workspace/Project-5/products/views.py
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart, CartItem
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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
    cart_items = []
    cart_count = 0  # Variable to store the number of items in the cart

    if request.user.is_authenticated:
        # Retrieve cart items from the database for logged-in users
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = cart.items.all()
        cart_count = cart_items.count()  # Count the number of cart items
    else:
        # Retrieve cart items from the session for anonymous users
        cart_ids = request.session.get('cart', [])
        cart_items = [get_object_or_404(Product, id=product_id) for product_id in cart_ids]
        cart_count = len(cart_items)  # Count the number of products in the session cart

    return render(request, 'cart/details.html', {'cart_items': cart_items, 'cart_count':cart_count})

def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.user.is_authenticated:
        # For logged-in users, find and delete the CartItem
        cart, created = Cart.objects.get_or_create(user=request.user)
        CartItem.objects.filter(cart=cart, product=product).delete()
    else:
        # For anonymous users, remove the product ID from the session
        cart = request.session.get('cart', set())
        if product_id in cart:
            cart.remove(product_id)
            request.session['cart'] = list(cart)  # Save the updated cart back to the session

    messages.success(request, f"{product.courseName} was removed from your cart.") #Messages for success

    return redirect('cart_detail')  # Redirect to the cart detail page or another desired page


@login_required
def checkout(request):
    # Retrieve the user's cart items
    cart = Cart.objects.get(user=request.user)
    cart_items = cart.items.all()
    if not cart_items:
        messages.error(request, "Your cart is empty.")
        return redirect('cart_detail')
    return render(request, 'checkout/checkout.html', {'cart_items':cart_items})


# @login_required
# def checkout(request):
#     # Retrieve the user's cart items
#     cart_items = CartItem.objects.filter(user=request.user)
#     if not cart_items:
#         messages.error(request, "Your cart is empty.")
#         return redirect('cart_detail')

#     # Calculate total cost
#     total_price = sum(item.price for item in cart_items)

#     # Payment processing logic here using Stripe
#     # In this placeholder, we'll assume payment is successful.
#     # If payment is successful, proceed with the order

#     # Clear the user's cart
#     cart_items.delete()

#     # Provide feedback to the user
#     messages.success(request, "Checkout successful! Thank you for your purchase.")
#     return redirect('order_confirmation')  # Redirect to an order confirmation page