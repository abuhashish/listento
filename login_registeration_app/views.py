from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from login_registeration_app.models import *
from django.contrib import messages
from django.db.models import Count
import bcrypt
# Create your views here.
def root(request):
    print(5)
    return redirect('/login')
def login (request):
    print(5)
    return render(request,"login.html")
def register(request):
    return render(request,'registeration.html')
def adduser(request):
    if 'user' in request.session :
        return redirect('/thoughts')
    errors=User.objects.basic_validator(request.POST)
    if len(errors)>0:
        for key,value in errors.items():
            messages.error(request,value)
        return redirect('/')
    else:
        hashpassword= bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        user=User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],password=hashpassword,email=request.POST['email'],username=request.POST['user_name'],birth_date=request.POST['birth_date'])
        request.session['user']={
            'id':user.id,
            'fname':user.first_name,
            'lname':user.last_name,
        }
        return redirect('/home')
def home(request):
    return render(request,'home.html')
def artists(request):
    return render(request,'artistspage.html')
def userprofile(req):
    return render(req,'userprofile.html')
def artistprofile(req):
    return render(req,'artistpage.html')
def songpage(req):
    return render(req,'songpage.html')
