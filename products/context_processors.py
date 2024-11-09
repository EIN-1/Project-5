from .models import Cart, CartItem, Product

def cart_count(request):
    cart_count = 0
    total_price = 0

    if request.user.is_authenticated:
        # For logged-in users: Retrieve cart items from the database
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = cart.items.all()
        cart_count = cart.items.count()
        total_price = sum(item.product.price for item in cart_items)
    else:
        # For anonymous users: Retrieve cart items from the session
        cart_ids = request.session.get('cart', [])
        cart_count = len(cart_ids)
        total_price = sum(Product.objects.get(id=product_id).price for product_id in cart_ids)

    return {'cart_count': cart_count, 'total_price': total_price}