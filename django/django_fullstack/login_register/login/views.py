from django.shortcuts import render,redirect,HttpResponse
from django.shortcuts import render, redirect
from login.models import *
from django.contrib import messages
import bcrypt


def index(request):
    return render(request,'index.html')

def register():    
    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()  
    print(pw_hash)    
    return redirect("/")

def login():
    user = User.objects.filter(username=request.POST['username']) 
    if user:
        logged_user = user[0] 
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            return redirect('/success')
    return redirect("/")
