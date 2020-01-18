from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from .forms import ProductForm, DishForm, IngForm, CreateWeekForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Product, Category, Dish, Ingredient, Week, ListDishesWeek, _weekDish, _dish
from django.contrib.auth.models import AnonymousUser
from random import randrange

def main(request):
    try:  
        listweek = Week.objects.filter(user_id = request.user)
        allWeek = list()      
        for i in listweek:
            tmp = _weekDish(i)          
            allDishes = ListDishesWeek.objects.filter(week=i)          
            for ii in allDishes:                
                allIngredients = Ingredient.objects.filter(dish=ii.dish)
                _dishtmp = _dish(ii)
                for ing in allIngredients:
                    _dishtmp.ingredients.append(ing)
                tmp.dishes.append(_dishtmp)  
            allWeek.append(tmp) 
        return render(request, 'menu/index.html', {'allWeek': allWeek})
    except:
        return redirect('loginmenu')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)        
        if form.is_valid():
            form.save()
            return redirect('loginmenu')
        else:            
            return render(request, 'menu/reg.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'menu/reg.html', {'form': form})

def loginmenu(request):    
    if request.method == 'POST':
            error = "Неверный логин или пароль"
            form = AuthenticationForm(request.POST)               
            user = authenticate(username=request.POST['username'], password=request.POST['password'])           
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('mymenu')
                else:                    
                    return render(request, 'menu/log.html', {'form': form, 'error': error})  
            else:
                return render(request, 'menu/log.html', {'form': form, 'error': error})                      
    else:
        form = AuthenticationForm()
        return render(request, 'menu/log.html', {'form': form})  

def logoutmenu(request):
    logout(request)
    return redirect('mymenu')

def showproduct(request):
    allprod = Product.objects.all()
    return render(request, 'menu/allprod.html', {'allprod': allprod})         

@login_required(login_url='loginmenu')
def addproduct(request):
    if request.method == 'POST':          
        form = ProductForm(request.POST)    
        if form.is_valid():  
            form.save()
            return redirect('allproduct') 
    else:
        form = ProductForm()
    return render(request, 'menu/addprod.html', {'form': form})    

def showdish(request):
    alldishes = Dish.objects.all()
    enddish = list()
    for i in alldishes:                
        allIngredients = Ingredient.objects.filter(dish=i)
        _dishtmp = _dish(i)
        for ing in allIngredients:
            _dishtmp.ingredients.append(ing)
        enddish.append(_dishtmp) 
    return render(request, 'menu/alldish.html', {'enddish': enddish})

@login_required(login_url='loginmenu')
def adddish(request):
    nameerror = ''
    dishcaterror = ''
    if request.method == 'POST':
        form = DishForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alldish')
        else:
            nameerror = 'Это поле обязательно'
            dishcaterror = 'Выберите категорию'
    else:
        form = DishForm()
    return render(request, 'menu/adddish.html', {'form': form, 'nameerror':nameerror, 'dishcaterror':dishcaterror })

def dishinfo(request, dish_id):
    dish_detail = get_object_or_404(Dish, pk=dish_id)
    dishing = Ingredient.objects.filter(dish=dish_detail)
    _dishtmp = _dish(dish_detail)
    _dishtmp.ingredients = dishing
    form = IngForm()
    return render(request, 'menu/dishinfo.html', {"dish_detail" : _dishtmp, 'form':form})

@login_required(login_url='loginmenu')
def deleteing(request, ing_id):
    ing_detail = get_object_or_404(Ingredient, pk=ing_id)
    ing_detail.delete()
    return dishinfo(request, ing_detail.dish.id)

@login_required(login_url='loginmenu')
def adding(request, dish_id):
    form = IngForm(request.POST)
    if form.is_valid():
        form.save()
        return dishinfo(request, dish_id)
    return dishinfo(request, dish_id)

def createweek(request):
    if request.method == 'POST':
        form = CreateWeekForm(request.POST)
        if form.is_valid():
            days = _getcategorybyday(form)
            _createweek(days, request)
            return redirect('mymenu')
        else:
            categories = Category.objects.all()
            return render(request, 'menu/createweek.html', {'categories': categories, 'error': "Нужно заполнить все поля"})
    else:
        categories = Category.objects.all()
        return render(request, 'menu/createweek.html', {'categories':categories, 'error':''})





def _getcategorybyday(form):
    days = list()
    days.append(form['day1'].value())
    days.append(form['day2'].value())
    days.append(form['day3'].value())
    days.append(form['day4'].value())
    days.append(form['day5'].value())
    days.append(form['day6'].value())
    days.append(form['day7'].value())
    return days

def _createweek(days, request):
    week = Week()
    week.user = request.user
    week.name = "Тест"
    week.save()
    for day in days:
        dishs = Dish.objects.filter(dishcategory = day)
        dishes = list()
        for i in dishs:
            dishes.append(i.id)
        catrange = len(dishes)
        listdish = ListDishesWeek()
        listdish.week = week
        query = Dish.objects.filter(id = dishes[randrange(catrange)])
        listdish.dish = query[0]
        listdish.save()






#api part 
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from .serializers import ProductSerializer, DishSerializer

class ProductView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({"Products": serializer.data})
    
    def post(self, request):
        product = request.data.get('product')
        print(request)
        serializer = ProductSerializer(data=product)
        if serializer.is_valid(raise_exception=True):
            prod_saved = serializer.save()
        return Response({"success": "Product '{}' created successfully".format(prod_saved.name)})

    def put(self, request, pk):
        saved_product = get_object_or_404(Product.objects.all(), pk=pk)
        data = request.data.get('product')
        serializer = ProductSerializer(instance=saved_product, data=data, partial=True)
        print(serializer)
        print(saved_product)
        if serializer.is_valid(raise_exception=True):
            saved_product = serializer.save()
            return Response({"success": "Product '{}' updated successfully".format(saved_product.name)})

    def delete(self, request, pk):
        product = get_object_or_404(Product.objects.all(), pk=pk)
        product.delete()
        return Response({"message": "Product with id `{}` has been deleted.".format(pk)}, status=204)


class DishView(APIView):
    def get(self, request):
        dishes = Dish.objects.all()
        serializer = DishSerializer(dishes, many=True)
        return Response({"Dish": serializer.data})