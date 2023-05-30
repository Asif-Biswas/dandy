from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    address = models.CharField(max_length=200, blank=True)


class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)


class Store(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='media/store_logos/')
    profile_picture = models.ImageField(upload_to='media/profile_pictures/')
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    contact_no = models.CharField(max_length=20)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    ratings = models.DecimalField(max_digits=3, decimal_places=1)
    display = models.BooleanField(default=False)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # You can add other fields specific to the Product model


