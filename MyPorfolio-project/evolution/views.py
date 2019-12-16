from datetime import date
from django.shortcuts import render
from .models import Player, Section, Theme, Phase, PhaseTheme, _phase, _theme

# Create your views here.
def main(request):   
    players = Player.objects
    phaseLast = Phase.objects.latest('startDate')
    phaseTheme = _gettheme(phaseLast)
    num = _progressPercent(phaseLast)   
    return render(request, 'evo/index.html', {'players': players, 'phase':phaseLast, 
    'num': num, 'themes': phaseTheme})

def themes(request):  
    sections = Section.objects.all()  
    allTheme = list()  
    for sec in sections:
        tmp = _theme(sec)       
        allthemes = Theme.objects.filter(section=sec)
        for ii in allthemes:
            tmp.themes.append(ii)  
        allTheme.append(tmp) 
        print(tmp.name)
        print(tmp.themes)
    return render(request, 'evo/themes.html', {'allTheme' : allTheme })   

def phases(request):
    phase = Phase.objects.all()  
    allPhases = list()  
    for i in phase:
        tmp = _phase(i)       
        allthemes = PhaseTheme.objects.filter(phase=i)
        for ii in allthemes:
            tmp.themes.append(ii.theme)  
        allPhases.append(tmp) 
    return render(request, 'evo/phases.html', {'allPhases' : allPhases })  
  


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