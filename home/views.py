from django.shortcuts import render
from django.core.paginator import Paginator
from products.models import Product
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return the index page """
    products = Product.objects.all()  # Fetch all products
    paginator = Paginator(products, 10) #Return 10 items per page

    # Get the page number from the request
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)  # This gets the current page’s data

    return render(request, 'home/index.html', {'page_obj': page_obj})


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

