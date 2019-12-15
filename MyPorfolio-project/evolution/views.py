from django.shortcuts import render
from .models import Player

# Create your views here.
def main(request):
    players = Player.objects
    return render(request, 'evo/index.html', {'players': players})

    
  
   