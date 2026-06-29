from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class Roles(models.Model):
    name = models.CharField(max_length=50)

class UserProfile(models.Model):

    preferred_contact_way = [
        ('phone','Phone'),
        ('telegram','Telegram'),
        ('email','Email'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=30)
    preferred_contact = models.CharField(max_length=10, choices=preferred_contact_way)
    role_id = models.ForeignKey(Roles, on_delete=models.CASCADE, default=1)


class Products(models.Model):

    in_stock_choices = [
        ('in_stock','In stock'),
        ('available_for_production','Available for production'),
        ('not_available','Not available'),
    ]
    name = models.CharField(max_length=255)
    amount_left = models.IntegerField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    image2 = models.ImageField(upload_to='products/', blank=True)
    image3 = models.ImageField(upload_to='products/', blank=True)
    leather_type = models.CharField(max_length=100)
    in_stock = models.CharField(max_length=30, choices=in_stock_choices)

class Orders(models.Model):

    delivery_method_choices = [
        ('yandex', 'Yandex delivery'),
        ('SDEK', 'SDEK delivery'),
        ('postal', 'Postal services'),
        ('ozon', 'Ozon delivery')
    ]

    status_choices = [
        ('pending','Pending'),
        ('confirmed','Confirmed'),
        ('in-production','In production'),
        ('shipped','Shipped'),
        ('delivered','Delivered'),
        ('cancelled','Cancelled'),
        ('delayed','Delayed'),
        ('returned','Returned'),
        ('closed','Closed'),
    ]
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=30, choices=status_choices)
    delivery_method = models.CharField(max_length=30, choices=delivery_method_choices)
    order_time = models.DateTimeField(auto_now_add=True)

class Custom_orders(models.Model):

    delivery_method_choices = [
        ('yandex', 'Yandex delivery'),
        ('SDEK', 'SDEK delivery'),
        ('postal', 'Postal services'),
        ('ozon', 'Ozon delivery')
    ]

    status_choices = [
        ('pending','Pending'),
        ('confirmed','Confirmed'),
        ('in-production','In production'),
        ('shipped','Shipped'),
        ('delivered','Delivered'),
        ('cancelled','Cancelled'),
        ('delayed','Delayed'),
        ('returned','Returned'),
        ('closed','Closed'),
    ]
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, choices=status_choices)
    delivery_method = models.CharField(max_length=30, choices=delivery_method_choices)
    order_time = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    leather_type = models.CharField(max_length=100)
    reference = models.URLField(blank=True)
    reference_2 = models.URLField(blank=True)
    reference_3 = models.URLField(blank=True)

class Basket_item(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    amount = models.IntegerField(blank=False, default=1)