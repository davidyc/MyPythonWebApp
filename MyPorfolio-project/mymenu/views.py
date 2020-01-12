from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from .forms import ProductForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Product, Category, Dish, Ingredient, Week, ListDishesWeek, _weekDish

def main(request):
    listweek = Week.objects.filter(user_id = request.user)
    allWeek = list()   
    for i in listweek:
        tmp = _weekDish(i)        
        allDishes = ListDishesWeek.objects.filter(week=i)
        for ii in allDishes:
            print(ii)
            tmp.dishes.append(ii)  
        allWeek.append(tmp) 
    return render(request, 'menu/index.html', {'allWeek': allWeek})

def addproduct(request):
    if request.method == 'POST':          
        form = ProductForm(request.POST)      
        if form.is_valid():  
            form.save()
            return HttpResponse("Done")     
    else:
        form = ProductForm()
    return render(request, 'menu/addprod.html', {'form': form})    

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
                print('DDD')
                return render(request, 'menu/log.html', {'form': form, 'error': error})                      
    else:
        form = AuthenticationForm()
        return render(request, 'menu/log.html', {'form': form})  

def logoutmenu(request):
    logout(request)
    return redirect('mymenu')