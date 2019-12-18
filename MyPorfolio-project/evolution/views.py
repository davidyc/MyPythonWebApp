from datetime import date
from django.shortcuts import render, get_object_or_404, redirect
from .models import Player, Section, Theme, Phase, PhaseTheme, _phase, _theme
from .forms import PhaseForm
import random

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
    hasCurrent = _hascurrent()     
    return render(request, 'evo/phases.html', {'allPhases' : allPhases, 'hasCurrent' : hasCurrent })  
 
  
def addphases(request):  
    if request.method == 'POST':          
        form = PhaseForm(request.POST)      
        if form.is_valid(): 
            _addnewphase(form)
                       
            # add page successful 
            return phases(request)          
    else:
        form = PhaseForm()
    return render(request, 'evo/addphases.html', {'form': form})    




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

def _hascurrent():
    phase = Phase.objects.latest('finishDate')  
    today = date.today()
    if today >= phase.finishDate:
        return None
    else:
        return phase

def _getnextphasenubmer():
    phase = Phase.objects.latest('number')  
    return phase.number + 1 

def _addnewphase(form):
    new_Phase = form.save(commit=False)
    new_Phase.startDate = date.today()             
    new_Phase.number = _getnextphasenubmer()
    new_Phase.save() 
    _addthemetophase(new_Phase)
     
def _addthemetophase(new_Phase):
    minCounttheme = 1
    daystotheme = 7
    countdays = (new_Phase.finishDate - new_Phase.startDate).days
    countthemes = countdays // daystotheme + minCounttheme
    


    
  


    
   
