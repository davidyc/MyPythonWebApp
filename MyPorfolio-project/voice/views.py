from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Candidate, Voice
from .forms import VoiceForm


class CandidateVoice:    
    def __init__(self, name, count, voices):       
        self.name = name
        self.count = count
        self.voices = voices


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

@login_required(login_url='loginmenu')
def show_allvoites(request): 
    htmldict = dict()  
    allcand = list()
    cands = Candidate.objects.all()
    voices = Voice.objects.all()
    _add_to_dict("voices", voices, htmldict)
    for cand in cands: 
        cand_voices = Voice.objects.filter(candidate=cand)
        tmp = CandidateVoice(cand.name, len(cand_voices), cand_voices)
        allcand.append(tmp)
        _add_to_dict("CandWithVoices", allcand, htmldict )
    return render(request, 'voice/showall.html', htmldict)

def detele_voice(request, voice_id):
    voice = get_object_or_404(Voice, id=voice_id)
    voice.delete()
    return redirect('showall')   



def _add_to_dict(key, value, newdict = dict()):
    newdict[key] = value
    return newdict
