
from django.views import View
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required 
def my_profile(request):
    user = request.user 
    return render(request, 'user_profile.html', {'user': user}) 

