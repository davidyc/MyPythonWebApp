from django.forms import ModelForm
from .models import Product, Category, Dish, Ingredient, Week, ListDishesWeek

# Create the form class.
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name']
