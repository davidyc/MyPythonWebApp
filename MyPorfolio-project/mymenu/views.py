from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

def main(request):
    return render(request, 'menu/index.html')


