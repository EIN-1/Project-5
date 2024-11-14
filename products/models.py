#/workspace/Project-5/products/models.py
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


User = get_user_model()


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()
    def __str__(self):
        return self.name
    
class Product(models.Model):    
    courseName = models.CharField(max_length=254)
    instructor = models.CharField(max_length=254)
    courseUrl = models.URLField(max_length=1024, null=True, blank=True)
    imageUrl = models.URLField(max_length=1024, null=True, blank=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    reviews = models.IntegerField(null=True, blank=True)
    duration = models.DecimalField(max_digits=6, decimal_places=2)
    lectures = models.IntegerField(null=True, blank=True)
    level = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    flag = models.BooleanField(default=False)
    students = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.courseName

    def get_absolute_url(self):
        return reverse('product-detail', args=[str(self.id)])

    class Meta:
        ordering = ['-students']

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    def __str__(self):
        return self.product.courseName

    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='orders')
    amount = models.IntegerField()
    stripe_id = models.CharField(max_length=255)
    status = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

class OrderItems(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.PROTECT)
    product = models.ForeignKey(Product, related_name='order_item', on_delete=models.PROTECT)
    price = models.IntegerField()

class Review(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_reviews', on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=2, decimal_places=1, min=1, max=5, default=1)  # e.g., 4.5 out of 5
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} review on {self.product}"

    class Meta:
        ordering = ['-created_at']