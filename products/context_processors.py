from .models import Cart, CartItem

def cart_count(request):
    cart_count = 0

    if request.user.is_authenticated:
        # For logged-in users: Retrieve cart items from the database
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_count = cart.items.count()
    else:
        # For anonymous users: Retrieve cart items from the session
        cart_ids = request.session.get('cart', [])
        cart_count = len(cart_ids)

    return {'cart_count': cart_count}