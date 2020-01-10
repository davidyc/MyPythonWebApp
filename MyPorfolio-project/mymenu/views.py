from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .forms import ProductForm

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

