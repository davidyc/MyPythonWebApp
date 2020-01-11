from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from .forms import ProductForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, login, authenticate


def main(request):
    return render(request, 'menu/index.html')

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
        print(form)
        if form.is_valid():
            form.save()
            return redirect('mymenu')
        else:
            return HttpResponse("user.is_active")    
    else:
        form = UserCreationForm()
        return render(request, 'menu/reg.html', {'form': form})


def loginmenu(request):    
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('mymenu')
                else:
                    return HttpResponse("user.is_active")     
            else:
                return HttpResponse(" user is not")     
                    
    else:
        form = AuthenticationForm()
        return render(request, 'menu/log.html', {'form': form})  

def logoutmenu(request):
    logout(request)
    return redirect('Home')