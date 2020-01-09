from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

def main(request):
    return HttpResponse('<h1>First view  for my beloved wife</h1>')


