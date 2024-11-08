# Inside /workspace/Project-5/technical_skills/views.py
from django.views import View
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required  # Ensures the user is logged in to view this page
def my_profile(request):
    user = request.user  # Access user data here if needed
    return render(request, 'user_profile.html', {'user': user})  # Pass user information to the template

