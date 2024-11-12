from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('newsletter', views.subscribe_newsletter, name='subscribe_to_news_letter'),
    path('faq', views.FaqView.as_view(), name="faq"),
    path('about', views.AboutView.as_view(), name="about"),
    path('privacy', views.PrivacyPolicyView.as_view(), name="privacy_policy"),
]
