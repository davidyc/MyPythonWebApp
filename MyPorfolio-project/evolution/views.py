from datetime import date
from django.shortcuts import render
from .models import Player, Section, Theme, Phase, PhaseTheme

# Create your views here.
def main(request):
    today = date.today()
    players = Player.objects
    phase = Phase.objects.get(id=2)
    return render(request, 'evo/index.html', {'players': players, 'phase':phase})

def themes(request):    
    sections = Section.objects
    themes = Theme.objects
    return render(request, 'evo/themes.html', {'sections' : sections, 'themes' : themes })   
  
   