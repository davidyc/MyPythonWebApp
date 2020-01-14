from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from .forms import ProductForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Product, Category, Dish, Ingredient, Week, ListDishesWeek, _weekDish, _dish
from django.contrib.auth.models import AnonymousUser

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

#api part 
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from .serializers import ProductSerializer


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