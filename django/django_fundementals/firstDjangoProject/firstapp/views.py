from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
def root(request):
    return redirect('/blogs')

def index(request):
    shatha = {
    	"name": "Noelle",
    	"favorite_color": "turquoise",
    	"pets": ["Bruce", "Fitz", "Georgie"]
    }
    return render(request, "index.html", shatha)
def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect('/')

def show(request, number):
    return HttpResponse(f"placeholder to display blog number: {number}")

def json(request):
    return JsonResponse({"response": "JSON response from redirected_method", "status": True})