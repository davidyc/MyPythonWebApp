from django.contrib import admin
from .models import Product, Category, Dish, Ingredient, Week, ListDishesWeek


# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Dish)
admin.site.register(Ingredient)
admin.site.register(Week)
admin.site.register(ListDishesWeek)
