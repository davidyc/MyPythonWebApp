from django.forms import ModelForm
from .models import Product, Category, Dish, Ingredient, Week, ListDishesWeek

# Create the form class.
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name']

class DishForm(ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'discription', 'dishcategory']

class IngForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ['product', 'dish']