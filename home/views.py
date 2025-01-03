from django.shortcuts import render
from django.core.paginator import Paginator
from products.models import Product, Category, OrderItems
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db.models import Q
from django.conf import settings
from django.contrib import messages
from django.views.generic import TemplateView
from .models import Carousel
from django.db.models import Exists, OuterRef
from mailchimp_marketing.api_client import ApiClientError
import mailchimp_marketing as MailChimpMarketing

mailchimp = MailChimpMarketing.Client()
mailchimp.set_config({
    'api_key': settings.MAILCHIMP_API_KEY,
    'server': settings.MAILCHIMP_REGION,
})
list_id = settings.MAILCHIMP_AUDIENCE_ID



def subscribe_newsletter(request):
    next_url = request.POST.get('next', '/')
    if request.method == 'POST':
        email = request.POST.get('email')
        print(email)
        member_info = {
            "email_address": email,
            "status":"subscribed",
        }
        try:
            response = mailchimp.lists.add_list_member(list_id, member_info)
            messages.success(request, "You've successfully subscribed to our newsletter!")
        except ApiClientError as error:
            messages.error(request, "There was an error subscribing. Please try again.")
    return redirect(next_url)


def index(request):
    """ A view to return the index page """
    query_params = request.GET.copy()  
    query_params.pop('page', None)  
    query_params_string = query_params.urlencode()    
    category_query = request.GET.get('category', None)
    search_query = request.GET.get('search', '')
    sort_field = request.GET.get('sort', 'courseName') 
    order = request.GET.get('order', 'asc') 
    
    products = Product.objects.all() 
    categories = Category.objects.all()
    carousel = Carousel.objects.filter(active=True)

   
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

    paginator = Paginator(products, 3) 

   
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) 

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
