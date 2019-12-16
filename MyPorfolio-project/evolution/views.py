from datetime import date
from django.shortcuts import render
from .models import Player, Section, Theme, Phase, PhaseTheme

# Create your views here.
def main(request):   
    players = Player.objects
    phaseLast = Phase.objects.latest('startDate')
    phaseTheme = _gettheme(phaseLast)
    num = _progressPercent(phaseLast)   
    return render(request, 'evo/index.html', {'players': players, 'phase':phaseLast, 
    'num': num, 'themes': phaseTheme})

def themes(request):   
    themes = Theme.objects
    return render(request, 'evo/themes.html', {'themes' : themes })   
  


def _gettheme(phaseLast):
    if phaseLast != None:
       return PhaseTheme.objects.filter(phase=phaseLast)
    else:
       return None

def _progressPercent(phaseLast : Phase):
    start = phaseLast.startDate    
    finish = phaseLast.finishDate
    today = date.today()
    maxpercent = (finish-start).days
    realpercent = (finish -today).days
    per = realpercent*100//maxpercent
    if per > 100 or per < 0:
        return 100
    return 100 - per