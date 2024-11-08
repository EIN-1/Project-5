from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .models import Cart, Product

#Copy cart for an anonymous user to the database
@receiver(user_logged_in)
def move_cart_to_database(sender, user, request, **kwargs):
    session_cart = request.session.get('cart', [])
    if session_cart:
        for product_id in session_cart:
            product = Product.objects.get(id=product_id)
            cart, created = Cart.objects.get_or_create(user=user, product=product)
        request.session['cart'] = []  # Clear the session cart
