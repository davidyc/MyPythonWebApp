from django.forms import ModelForm
from django import forms
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


class CreateWeekForm(forms.Form):
    day1 = forms.IntegerField()
    day2 = forms.IntegerField()
    day3 = forms.IntegerField()
    day4 = forms.IntegerField()
    day5 = forms.IntegerField()
    day6 = forms.IntegerField()
    day7 = forms.IntegerField()
    name = forms.CharField(max_length=20)
