import operator

from random import randrange

from .forms import ProductForm, DishForm, IngForm, CreateWeekForm
from .models import Product, Category, Dish, Ingredient, Week, ListDishesWeek, _weekDish, _dish

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect



def main(request):
    try:  
        listweek = Week.objects.filter(user_id = request.user)
        allWeek = _getallweek(listweek)          
        if len(allWeek)>0:
            return render(request, 'menu/index.html', {'week': allWeek[-1]})
        return render(request, 'menu/index.html', {'week': None})
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
    sortallprod = sorted(allprod, key=operator.attrgetter('name'))
    return render(request, 'menu/allprod.html', {'allprod': sortallprod})         

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

@login_required(login_url='loginmenu')
def createweek(request):
    if request.method == 'POST':
        form = CreateWeekForm(request.POST)
        if form.is_valid():
            days = _getcategorybyday(form)
            _createweek(days, request, form['name'].value())
            return redirect('mymenu')
        else:
            categories = Category.objects.all()            
            return render(request, 'menu/createweek.html', {'categories': categories, 'error': "Нужно заполнить все поля"})
    else:
        categories = Category.objects.all()
        return render(request, 'menu/createweek.html', {'categories':categories, 'error':''})



def _getallweek(listweek):
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
    return allWeek     

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

def _createweek(days, request, name):
    week = Week()
    week.user = request.user
    week.name = name
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
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer, CategorySerializer, DishSerializer, IngredientSerializer

@api_view(['GET', 'POST'])
def apiallprod(request):
    if request.user.is_anonymous != True:
        print(request.user.is_anonymous)
        if request.method == 'GET':
            product = Product.objects.all()
            serializer = ProductSerializer(product, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("Unauthorized", status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET', 'PUT', 'DELETE'])
def apiprod(request, pk):
    if request.user.is_anonymous != True:
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = ProductSerializer(product)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = ProductSerializer(product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response("Unauthorized", status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET', 'POST'])
def apiallcat(request):
    if request.user.is_anonymous != True:
        if request.method == 'GET':
            categies = Category.objects.all()
            serializer = CategorySerializer(categies, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = CategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("Unauthorized", status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET', 'PUT', 'DELETE'])
def apicat(request, pk):
    if request.user.is_anonymous != True:
        try:
            category = Category.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = CategorySerializer(category)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = CategorySerializer(category, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            category.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response("Unauthorized", status=status.HTTP_401_UNAUTHORIZED)
    
    
@api_view(['GET', 'POST'])
def apialldish(request):
    if request.user.is_anonymous != True:
        if request.method == 'GET':
            dish = Dish.objects.all()
            serializer = DishSerializer(dish, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = DishSerializer(data=request.data)        
            if serializer.is_valid(): 
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("Unauthorized", status=status.HTTP_401_UNAUTHORIZED)    
    

@api_view(['GET', 'PUT', 'DELETE'])
def apidish(request, pk):
    if request.user.is_anonymous != True:
        try:
            dish = Dish.objects.get(pk=pk)        
        except Dish.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
        serializer = DishSerializer(dish)
        return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = DishSerializer(dish, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            dish.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response("Unauthorized", status=status.HTTP_401_UNAUTHORIZED)    


@api_view(['GET', 'POST'])
def apialling(request):
    if request.user.is_anonymous != True:
        if request.method == 'GET':
            ing = Ingredient.objects.all()
            serializer = IngredientSerializer(ing, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = IngredientSerializer(data=request.data)        
            if serializer.is_valid(): 
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("Unauthorized", status=status.HTTP_401_UNAUTHORIZED)    

@api_view(['GET', 'PUT', 'DELETE'])
def apiing(request, pk):
    if request.user.is_anonymous != True:
        try:
            ing = Ingredient.objects.get(pk=pk)        
        except Ingredient.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
        serializer = IngredientSerializer(ing)
        return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = IngredientSerializer(ing, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            dish.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'POST'])
def apiallweek(request):
    if request.user.is_anonymous != True:
        if request.method == 'GET':
            ing = Ingredient.objects.all()
            serializer = IngredientSerializer(ing, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = IngredientSerializer(data=request.data)        
            if serializer.is_valid(): 
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("Unauthorized", status=status.HTTP_401_UNAUTHORIZED)    

@api_view(['GET', 'PUT', 'DELETE'])
def apiweek(request, pk):
    if request.user.is_anonymous != True:
        try:
            ing = Ingredient.objects.get(pk=pk)        
        except Ingredient.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
        serializer = IngredientSerializer(ing)
        return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = IngredientSerializer(ing, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            dish.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    


