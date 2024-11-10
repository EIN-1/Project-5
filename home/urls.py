from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('newsletter', views.subscribe_newsletter, name='subscribe_to_news_letter')
]
