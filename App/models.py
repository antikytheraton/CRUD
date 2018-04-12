from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    manager = models.CharField(max_length=30)

class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menus')
    name = models.CharField(max_length=30)

class Product(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='products')
    description = models.CharField(max_length=50)
