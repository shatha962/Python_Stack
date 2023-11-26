from django.shortcuts import render, redirect
import random

# Create your views here
def index(request):
    randInt = random.randint(1, 100)
    if 'rand' not in request.session:
        request.session['rand'] = randInt
    print(request.session['rand'])
    return render(request, 'index.html')

def process(request):
    input = request.POST['input']
    if int(input) > request.session['rand']:
        text = "Too High!"
        color = 'red'
    elif int(input) < request.session['rand']:
        text = "Too Low!"
        color = 'red'
    elif int(input) == request.session['rand']:
        text = f"{request.session['rand']} Was the number"
        color = 'green'
    context = {
        'input' : input,
        'text' : text,
        'color' :color
    }
    return render(request, 'index.html', context)

def replay(request):
    del request.session['rand']
    return redirect('/')