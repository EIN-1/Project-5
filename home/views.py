from django.shortcuts import render
from django.core.paginator import Paginator
from products.models import Product, Category
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db.models import Q
from mailchimp_marketing import Client
from django.conf import settings
from django.contrib import messages
from django.views.generic import TemplateView
from .models import Carousel

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
    query_params = request.GET.copy()  # Create a mutable copy of the query parameters
    query_params.pop('page', None)  # Remove any existing 'page' parameter
    query_params_string = query_params.urlencode()  # Convert to query string
    # Get the category filter
    category_query = request.GET.get('category', None)
    # Get the search query from the request
    search_query = request.GET.get('search', '')
    sort_field = request.GET.get('sort', 'courseName')  # Default field
    order = request.GET.get('order', 'asc')  # Default order
    
    products = Product.objects.all()  # Fetch all products
    categories = Category.objects.all()
    carousel = Carousel.objects.filter(active=True)

    print(query_params_string)

    # Add "-" for descending order
    sort_option = f"{'' if order == 'asc' else '-'}{sort_field}"
    # Validate the sort field to prevent SQL injection
    valid_fields = ['courseName', 'rating', 'reviews', 'price']
    if sort_field not in valid_fields:
        sort_option = 'courseName'  # Fallback to default
    
    products = Product.objects.all().order_by(sort_option)

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

    paginator = Paginator(products, 3) #Return 6 items per page

    # Get the page number from the request
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)  # This gets the current page’s data

    return render(request, 'home/index.html', {'page_obj': page_obj, 'query_params': query_params_string, 'categories':categories, 'carousel':carousel})


@login_required
def profile_view(request):
    return render(request, 'account/profile.html')


class PrivacyPolicyView(TemplateView):
    template_name = "home/privacy_policy.html"

class FaqView(TemplateView):
    template_name = "home/faq.html"

class AboutView(TemplateView):
    template_name = "home/about.html"
