from django.shortcuts import render
import apiai, json

# Create your views here.
def main(request):   
    print(_getresponse('Привет'))
    return render(request, 'bot/index.html')


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
        return "Я не понимаю"