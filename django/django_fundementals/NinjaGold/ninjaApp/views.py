from django.shortcuts import render, HttpResponse, redirect
import random
from time import gmtime, strftime

# def index(request):
#     if 'gold' not in request.session:
#         request.session['gold'] = 0
#         request.session['activities'] = []
#         request.session['color'] = "green"
#     context = {
#         'gold' : request.session['gold'],
#         # 'activities1' : request.session['activities'],
#         # 'color' : request.session['color']
#     }
#     return render(request, 'main.html', context )

# def process(request):
#     time = strftime("%Y-%m-%d %H:%M %p", gmtime())
#     if request.POST['action'] == "farm" or request.POST['action'] == "cave" or request.POST['action'] == "house":
#         randGold = random.randint(10,20)
#         request.session['gold'] += randGold
#         text = f"You entered a {request.POST['action']} and earned {randGold}. {time}"
#         request.session['activities'].insert(0, text)
#         request.session.save()
#         request.session['color'] = "green"

#     elif request.POST['action'] == "quest":
#         randGold = random.randint(-50,50)
#         request.session['gold'] += randGold
#         if randGold > 0 :
#             text = f"You entered a {request.POST['action']} and earned {randGold}. {time}"
#             request.session['color'] = "green"
#         else:
#             text = f"You entered a {request.POST['action']} and lost {randGold}. {time}"
#             request.session['color'] = "red"
            
#         request.session['activities'].insert(0, text)
#         request.session.save()
#     print(request.session['activities'])
#     return redirect('/')
        
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if request.method == 'POST':
        process(request)

    return render(request, 'main.html')

def process(request):
    time = strftime("%Y-%m-%d %H:%M %p", gmtime())
    if request.POST['action'] == "farm" or request.POST['action'] == "cave" or request.POST['action'] == "house":
        randGold = random.randint(10,20)
        request.session['gold'] += randGold
        text = f"You entered a {request.POST['action']} and earned {randGold}. {time}"
        color = "green"

    elif request.POST['action'] == "quest":
        randGold = random.randint(-50,50)
        request.session['gold'] += randGold
        if randGold > 0:
            text = f"You entered a {request.POST['action']} and earned {randGold}. {time}"
            color = "green"
        else:
            text = f"You entered a {request.POST['action']} and lost {randGold}. {time}"
            color = "red"

    if 'activities' not in request.session:
        request.session['activities'] = []
    request.session['activities'].insert(0, {"text": text, "color": color})
    request.session.save()

def replay(request):
    del request.session['gold']
    del request.session['activities']
    return redirect('/')