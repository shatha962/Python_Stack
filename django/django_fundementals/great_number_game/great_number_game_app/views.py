from django.shortcuts import render, HttpResponse
import random

# Create your views here.
def index(request):
    randomNumber = random.randint(1, 100)
    request.session['random'] = randomNumber
    return render(request, 'index.html')

def process(request):
    input = int(request.POST['number'])
    print(request.session['random'] )
    if request.session['random'] == input:
        text = f"{request.session['random']} was the number"
        color = "green"
    elif request.session['random'] > input:
        text = "Too Low!"
        color = "red"
    elif request.session['random'] < input:
        text = "Too high!"
        color = "red"
    
    context = {
        'color' : color,
        'text' : text
    }
    return render(request, 'index.html', context)