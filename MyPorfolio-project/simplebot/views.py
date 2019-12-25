from django.shortcuts import render
from .forms import WordForm
import apiai, json, datetime

dialogs = list()   
name = ''

# Create your views here.
def main(request):  
    userform = WordForm()
    return render(request, 'bot/index.html', {"form" : userform})

def dialog(request): 
    userform = WordForm()
    if request.method == "POST":  
        global name   
        say = request.POST.get("word")      
        told = dialoguser(name, say)
        dialogs.append(told)   

        answer = _getresponse(say)    
        told = dialoguser("Bender", answer)
        dialogs.append(told)   
    else:
        dialogs.clear()
        name = request.GET.get("word")          
   
    return render(request, 'bot/dialog.html', {'dialog': dialogs, "form" : userform })


def _getresponse(text):
    request = apiai.ApiAI('710a5fa1d9cf4d14af93e3eacf38294a').text_request()
    request.lang = 'ru'
    request.session_id = 'SimpleBot'
    request.query = text
    responsejson = json.loads(request.getresponse().read().decode('utf-8'))   
    response = responsejson['result']['fulfillment']['speech']

    if response:
        return response
    else:
        return "Я не понимаю."

class dialoguser:
    def __init__(self, name, say):
        self.name = name
        self.say = say
        self.time = datetime.datetime.now()    
    
    def __lt__(self, other):
        if self.time < self.time:
            return True
        else: 
            return False

    def __lt__(self, other):
        if self.time > self.time:
            return True
        else: 
            return False
