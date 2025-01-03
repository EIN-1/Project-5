
import stripe
from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart, CartItem, Order, OrderItems, Category, Review
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.db import transaction
from django.db.models import Q, Sum
from django.views.decorators.csrf import csrf_exempt
import json
from django.db.models import Exists, OuterRef
from django.http import JsonResponse
from .emails import send_checkout_email
from .forms import ReviewForm, CreateCourseForm, OrderEditForm, EditCourseForm


stripe.api_key = settings.STRIPE_SECRET_KEY


def list_all_products(request):
    query_params = request.GET.copy() 
    query_params.pop('page', None) 
    query_params_string = query_params.urlencode()
    category_query = request.GET.get('category', None)
    search_query = request.GET.get('search', '')
    sort_field = request.GET.get('sort', 'courseName') 
    order = request.GET.get('order', 'asc')

    products = Product.objects.all()
    categories = Category.objects.all()
    
    sort_option = f"{'' if order == 'asc' else '-'}{sort_field}"
    valid_fields = ['courseName', 'rating', 'reviews', 'price']
    if sort_field not in valid_fields:
        sort_option = 'courseName' 
    
    products = Product.objects.all().order_by(sort_option)

    if request.user.is_authenticated:
        products = products.annotate(
            has_purchased=Exists(
                OrderItems.objects.filter(product=OuterRef('pk'), order__user=request.user)
            )
        )

    if category_query:
        products = products.filter(
            category=category_query
        )

    if search_query:
        products = products.filter(
            Q(courseName__icontains=search_query) |
            Q(category__name__icontains=search_query) |
            Q(level__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(flag__icontains=search_query) |
            Q(instructor__icontains=search_query)
        )

    paginator = Paginator(products, 6) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'products/products.html', {'page_obj': page_obj, 'query_params': query_params_string, 'search_query': search_query, 'categories': categories })

def retrieve_product(request, id):
    product = Product.objects.get(id=id)
    reviews = product.product_reviews.all()

    return render(request, 'products/product.html', {'product':product, 'reviews':reviews, 'purchased': product.has_user_purchased(request.user) })


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    next_url = request.GET.get('next', '/')

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    else:
        cart = request.session.get('cart', set())
        cart = set(cart)
        cart.add(product_id)
        request.session['cart'] = list(cart)
    messages.success(request, message='Item successfully added to cart')

    return redirect(next_url)
def cart_detail(request):
    cart_items = []
    cart_count = 0 

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = cart.items.all()
        cart_count = cart_items.count() 
    else:
        cart_ids = request.session.get('cart', [])
        cart_items = [get_object_or_404(Product, id=product_id) for product_id in cart_ids]
        cart_count = len(cart_items)

    return render(request, 'cart/details.html', {'cart_items': cart_items, 'cart_count':cart_count})

def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        CartItem.objects.filter(cart=cart, product=product).delete()
    else:
        cart = request.session.get('cart', set())
        if product_id in cart:
            cart.remove(product_id)
            request.session['cart'] = list(cart)  

    messages.success(request, f"{product.courseName} was removed from your cart.") 

    return redirect('cart_detail')  

@login_required
def checkout(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = cart.items.all()
    if not cart_items:
        messages.error(request, "Your cart is empty.")
        return redirect('cart_detail')
    total_price = sum(item.product.price for item in cart_items)
    stripe_total = int(total_price * 100)
    try:
        payment_intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency='usd',
            metadata={'user_id': request.user.id}
        )
    except Exception as e:
        messages.error(request, f"Stripe error: {e}")
        return redirect('cart_detail')
    context = {
        'total_price': total_price,
        'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY,
        'client_secret': payment_intent['client_secret'],
        'cart_items': cart_items
    }

    return render(request, 'checkout/checkout.html', context)

@login_required
def order_confirmation(request):
    return render(request, 'orders/order-confirmation.html')

@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user)
    paginator = Paginator(orders, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'orders/orders.html', {'page_obj':page_obj, 'orders':orders})


@login_required
def order_details(request, order_id):
    order = Order.objects.get(id=order_id)
    items = order.items.all()
    return render(request, 'orders/order-detail.html', {'order': order, 'items':items})


@login_required
@csrf_exempt
def complete_payment(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        payment_intent_id = data.get('paymentIntentId')
        if not payment_intent_id:
            return JsonResponse({"success": False, "error": "Invalid payment."}, status=400)
        try:
            payment_intent = stripe.PaymentIntent.retrieve(payment_intent_id)
            order = None
            if payment_intent.status == 'succeeded':
                with transaction.atomic():
                    cart = Cart.objects.get(user=request.user)
                    cart_items = cart.items.all()
                    total_price = sum(item.product.price for item in cart_items)

                    order = Order.objects.create(
                        user=request.user,
                        amount=total_price,
                        stripe_id=payment_intent_id,
                        status="Completed"
                    )
                    for cart_item in cart_items:
                        OrderItems.objects.create(
                            order=order,
                            product=cart_item.product,
                            price=cart_item.product.price,
                        )
                    cart_items.delete()
                send_checkout_email(request.user.email, order)
                    

                return JsonResponse({"success": True})

            else:
                return JsonResponse({"success": False, "error": "Payment not completed."}, status=400)

        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)}, status=400)

    return JsonResponse({"success": False, "error": "Invalid request method."}, status=400)


@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product = product
            review.save()
            return redirect('product-detail', id=product_id)
    else:
        form = ReviewForm()
    return render(request, 'products/add_review.html', {'form': form, 'product': product})


@login_required
@staff_member_required
def create_course(request):
    if request.method == 'POST':
        form = CreateCourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.save()
            return redirect('management_dashboard') 
    else:
        form = CreateCourseForm()

    return render(request, 'products/admin/create_course.html', {'form': form})

@login_required
@staff_member_required
def edit_course(request, course_id):
    course = get_object_or_404(Product, id=course_id)

    if request.method == 'POST':
        form = EditCourseForm(request.POST, instance=course)
        if form.is_valid():
            messages.success(request, 'Course Updated Successfully')
            form.save() 
            return redirect('management_dashboard') 
    else:
        form = EditCourseForm(instance=course) 

    return render(request, 'products/admin/edit_course.html', {'form': form, 'course': course})

@login_required
@staff_member_required
def delete_course(request, course_id):
    course = get_object_or_404(Product, id=course_id)
    
    if request.method == 'POST':
        try:
            course.delete()
            messages.success(request, f'Course "{course.courseName}" has been deleted.')
        except:
            messages.error(request,"Can not delete item right now.")
        return redirect('products')  

    return render(request, 'products/admin/confirm_delete_course.html', {'course': course})

@staff_member_required  
def all_orders(request):
    sort_field = request.GET.get('sort', 'user__name') 
    order = request.GET.get('order', 'asc')
    search_query = request.GET.get('search', '')

    orders = Order.objects.all().order_by('-date') 
    valid_fields = ['user__name', 'amount', 'status', 'date']
    if sort_field not in valid_fields:
        sort_field = 'user__name'

    sort_option = f"{'' if order == 'asc' else '-'}{sort_field}"

    if search_query:
        orders = orders.filter(
            Q(user__username__icontains=search_query) |
            Q(amount__icontains=search_query) |
            Q(status__icontains=search_query) |
            Q(date__icontains=search_query) 
        )

   
    query_params = request.GET.copy()
    query_params.pop('page', None)

    paginator = Paginator(orders, 6)  
   
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)  


    cancelled = orders.filter(status='Cancelled').count()
    completed = orders.filter(status='Completed').count()
    total = Order.objects.all().count()
    pending = orders.filter(status='Pending').count()
    context = {
        'orders': page_obj, 
        'cancelled':cancelled,
        'completed':completed,
        'total':total,
        'pending':pending
    }
    return render(request, 'products/admin/all_orders.html', context)

@staff_member_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'products/admin/order_detail.html', {'order': order})

@staff_member_required
def edit_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)  
    if request.method == 'POST':
        form = OrderEditForm(request.POST, instance=order)
        if form.is_valid():
            form.save() 
            messages.success(request, "Order updated Successfully!")
            return redirect('admin_orders') 
    else:
        form = OrderEditForm(instance=order) 

    return render(request, 'products/admin/edit_order.html', {'form': form, 'order': order})

@staff_member_required
def management_dashboard(request):
    sort_field = request.GET.get('sort', 'courseName')  
    order = request.GET.get('order', 'asc')  
    search_query = request.GET.get('search', '')
    valid_fields = ['courseName', 'instructor', 'category', 'price', 'rating']
    if sort_field not in valid_fields:
        sort_field = 'courseName'

    sort_option = f"{'' if order == 'asc' else '-'}{sort_field}"

    order_count = Order.objects.all().count()
    product_count = Product.objects.all().count()
    total_sales = Order.objects.filter(status="Completed").aggregate(Sum('amount'))['amount__sum'] or 0
    potential_sales = Product.objects.aggregate(Sum('price'))['price__sum'] or 0
    products = Product.objects.all().order_by(sort_option)

    if search_query:
        products = products.filter(
            Q(courseName__icontains=search_query) |
            Q(category__name__icontains=search_query) |
            Q(level__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(flag__icontains=search_query) |
            Q(instructor__icontains=search_query)
        )

    query_params = request.GET.copy()
    query_params.pop('page', None) 

    paginator = Paginator(products, 6)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) 

    context = {
        "order_count": order_count,
        "product_count": product_count,
        "total_sales": total_sales,
        "products": page_obj,
        "potential_sales": potential_sales,
        "query_params": query_params.urlencode()
    }
    return render(request,"products/admin/products_dashboard.html", context)

@staff_member_required
def order_management_dashboard(request):
    order_count = Order.objects.all().count()
    product_count = Product.objects.all().count()
    total_sales = Order.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    potential_sales = Product.objects.aggregate(Sum('price'))['price__sum'] or 0
    orders = Order.objects.all()
    context = {
        "order_count": order_count,
        "product_count": product_count,
        "total_sales": total_sales,
        "orders": orders,
        "potential_sales": potential_sales
    }
    return render(request,"products/admin/orders_dashboard.html", context)

@login_required
def my_classes(request):
    courses = Product.objects.filter(
        order_item__order__user=request.user,
        order_item__order__status='Completed'
    ).distinct()
    paginator = Paginator(courses, 4)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
    }
    return render(request,"courses/list.html", context)

@login_required
def my_class(request, course_id):
    course = Product.objects.get(id=course_id)
    form = ReviewForm()
    if course.has_user_purchased(request.user):
        reviews = course.product_reviews.all()
        return render(request, "courses/content.html", { 'course':course, 'form':form, 'reviews': reviews })
    else:
        messages.error(request, "You don't own this course!")
        return redirect('my_classes')

