from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from .models import Course
# Create your views here.
def index(request):
    context = {
        "all_courses" : Course.objects.all()
    }
    return render(request, "home.html", context)

def add(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        name = request.POST['name']
        desc = request.POST['description']
        coarse = Course.objects.create(name = name, description = desc)

    return redirect('/')

def destroy_form(request, id):
    context = {
        'course' : Course.objects.get(id=id)
    }
    return render(request, 'destroy.html', context)

def destroy(request, id):
    course = Course.objects.get(id=int(id))
    course.delete()

    return redirect('/')