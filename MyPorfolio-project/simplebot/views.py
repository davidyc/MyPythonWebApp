from django.shortcuts import render
import apiai, json, datetime

# Create your views here.
def main(request):   
    return render(request, 'bot/index.html')

def dialog(request):   
    answer = _getresponse('Ты скучный')
    told = dialoguser("Bender", answer)
    dialogs = list()
    dialogs.append(told)
    print(dialogs)
    return render(request, 'bot/dialog.html', {'dialog': dialogs})


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
    def __str__(self):
        return "ssd"
