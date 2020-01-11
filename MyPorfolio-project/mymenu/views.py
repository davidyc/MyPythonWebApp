from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from .forms import ProductForm
from django.contrib.auth.forms import UserCreationForm

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
        if form.is_valid():
            form.save()
            return redirect('Home')
    else:
        form = UserCreationForm()
        return render(request, 'menu/reg.html', {'form': form})