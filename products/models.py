#/workspace/Project-5/products/models.py
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver


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

    def average_rating(self):
        if self.product_reviews.exists():
            return int(self.product_reviews.aggregate(models.Avg('rating'))['rating__avg'])
        return None

    def has_user_purchased(self, user):
        """Check if a specific user has purchased this product."""
        if user.is_authenticated:
            return OrderItems.objects.filter(order__user=user, product=self).exists()
        return False

    def get_purchase_count(self):
        from django.db.models import Count
        return OrderItems.objects.filter(
            product=self
        ).aggregate(Count('order__user', distinct=True))['order__user__count']

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
    product = models.ForeignKey(Product, related_name='product_reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_reviews', on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=2, decimal_places=1,default=1)  # e.g., 4.5 out of 5
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} review on {self.product}"

    class Meta:
        ordering = ['-created_at']

# Signal to update product rating and review count
@receiver(post_save, sender=Review)
def update_product_reviews(sender, instance, **kwargs):
    product = instance.product

    # Count total reviews and calculate average rating
    reviews_count = product.reviews
    average_rating = product.rating

    # Update product fields
    product.reviews = int(reviews_count) + 1
    product.rating = round(average_rating/(product.students+1), 2)  # Round to 2 decimal places for consistency
    product.save()