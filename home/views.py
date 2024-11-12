from django.shortcuts import render
from django.core.paginator import Paginator
from products.models import Product, Category
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db.models import Q
from mailchimp_marketing import Client
from django.conf import settings
from django.contrib import messages

mailchimp = Client()
mailchimp.set_config({
  'api_key': settings.MAILCHIMP_API_KEY,
  'server': settings.MAILCHIMP_REGION,
})


def subscribe_newsletter(request):
    next_url = request.POST.get('next', '/')
    if request.method == 'POST':
        email = request.POST.get('email')
        # try:
        member_info = {
            'email_address': email,
            'status': 'subscribed',
        }
        response = mailchimp.lists.add_list_member(
            settings.MAILCHIMP_AUDIENCE_ID,
            member_info,
        )
        messages.success(request, "You've successfully subscribed to our newsletter!")
        # except:
        #     messages.error(request, "There was an error subscribing. Please try again.")
    return redirect(next_url)


# Create your views here.

def index(request):
    """ A view to return the index page """
    # Get the category filter
    category_query = request.GET.get('category', None)
    # Get the search query from the request
    search_query = request.GET.get('search', '')
    products = Product.objects.all()  # Fetch all products
    categories = Category.objects.all()

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

    paginator = Paginator(products, 6) #Return 10 items per page

    # Get the page number from the request
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)  # This gets the current page’s data

    return render(request, 'home/index.html', {'page_obj': page_obj, 'categories':categories})


    # print("products in database =",products)
    # total_products = products.count()  # Count total products
    # context = {
    #     'total_products': total_products,
    #     'products': products,
    # }

    # return render(request, 'home/index.html',context)

@login_required
def profile_view(request):
    return render(request, 'account/profile.html')

