from django.shortcuts import render, redirect
from .models import Candidate, Voice
from .forms import VoiceForm

# Create your views here.
def main(request):        
    form = VoiceForm()    
    return render(request, 'voice/index.html', {"form": form})
    

def voite(request):   
    if request.method == 'POST':     
        form = VoiceForm(request.POST)                  
        if form.is_valid(): 
            form.save()           
            return redirect('voited')   
    return render(request, 'voice/voited.html')

def show_allvoites(request):   
    voices = Voice.objects.all()
    return render(request, 'voice/showall.html', {"voices" : voices})
