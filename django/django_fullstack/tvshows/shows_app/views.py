from django.shortcuts import render,HttpResponse, redirect
from .models import Show

# Create your views here.
def index(request):
    return redirect("/shows")

# main page
def all_shows(request):
    return render(request, "all_shows.html")

# create a show
def add_page(request):
    return render(request, "add_show.html")

def create(request):
    title = request.POST['title']
    network = request.POST['network']
    description = request.POST['description']
    release_date = request.POST['release_date']
    show = Show.objects.create(title = title, network = network,
                description = description, release_date = release_date)
    return redirect('/show/' + str(show.id))

def show(request, id):
    print("hi")
    context = {
        "show": Show.objects.get(id=int(id)),
    }
    print(Show.objects.get(id=int(id)))
    return render(request, "show.html", context)