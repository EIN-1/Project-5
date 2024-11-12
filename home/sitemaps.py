# sitemaps.py (create this file in your main app)
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from products.models import Product, Category

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return ['about', 'privacy_policy', 'faq']

    def location(self, item):
        return reverse(item)


class ProductSitemap(Sitemap):
    priority = 0.8
    changefreq = 'daily'

    def items(self):
        return Product.objects.all()

