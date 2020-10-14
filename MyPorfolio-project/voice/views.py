from django.shortcuts import render
from .models import Candidate

# Create your views here.
def main(request):   
    candidates = Candidate.objects
    return render(request, 'voice/index.html' )
