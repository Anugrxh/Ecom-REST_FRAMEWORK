from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Product, Cart, Rating, Order

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Rating)
admin.site.register(Order)
