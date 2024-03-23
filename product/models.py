from django.db import models

from user.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateTimeField('Product created date', auto_now_add=True)
    updated_date = models.DateTimeField('Product Updated date', auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, default=None, related_name='renter')
    price = models.CharField(max_length=10)
    discount = models.CharField(max_length=10, null=True, blank=True)
    created_date = models.DateTimeField('Product created date', auto_now_add=True)
    updated_date = models.DateTimeField('Product Updated date', auto_now=True)
    product_photo_url = models.URLField(max_length=300, blank=True, null=True)

    def __str__(self):
        return f"{self.name}-{self.id}"


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField('Product created date', auto_now_add=True)
    updated_date = models.DateTimeField('Product Updated date', auto_now=True)

    def __str__(self):
        return f"{self.user.username}-{self.id}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_date = models.DateTimeField('Product created date', auto_now_add=True)
    updated_date = models.DateTimeField('Product Updated date', auto_now=True)
