from django.shortcuts import render, redirect
from .models import Candidate
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
