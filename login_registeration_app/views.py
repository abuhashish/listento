from music_app.models import Music
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from login_registeration_app.models import *
from django.contrib import messages
from django.db.models import Count
import bcrypt
# Create your views here.
def root(request):
    return redirect('/login')
def login (request):
    if 'user' not in request.session:
        return render(request,"login.html")
    return redirect('/home')
def logins(req):
    user = User.objects.filter(username = req.POST['username'])
    psswd = req.POST['passwd'] 
    if user:
        logged_user=user[0]
        if bcrypt.checkpw(psswd.encode(), logged_user.password.encode()):
            req.session['user']={
                'fname':logged_user.first_name,
                'lname':logged_user.last_name,
                'id':logged_user.id,
                
            }
            context= {
                'userimg' : User.objects.get(id=req.session['user']['id']),
                'allimgs' : User.objects.all()
            }
        return render(req,'home.html',context)
    return redirect('/')
def register(request):
    return render(request,'registeration.html')
def home(req):
    if 'user' in req.session:
        allmusic = Music.objects.all
        context = {
        'allmusic':allmusic
        }
        return render(req,'home.html',context)
    return redirect('/')
def adduser(request):
    if 'user' in request.session :
        return redirect('/register')
    errors=User.objects.basic_validator(request.POST)
    if len(errors)>0:
        for key,value in errors.items():
            messages.error(request,value)
        return redirect('/')
    else:
        hashpassword= bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        user=User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        password=hashpassword,
        email=request.POST['email'],
        username=request.POST['user_name'],
        birh_date=request.POST['birth_date'],
        gender=Gender.objects.get(id=request.POST['gender']),
        image=request.FILES['img'],
        role=Role.objects.get(id=2)
        )
        request.session['user']={
            'id':user.id,
            'fname':user.first_name,
            'lname':user.last_name,
        }
        return redirect('/home')
def artists(request):
    return render(request,'artistspage.html')
def userprofile(req):
    context={
        'x':User.objects.get(id=req.session['user']['id'])
    }
    
    return render(req,'userprofile.html',context)
def artistprofile(req):
    allmusic = Music.objects.all
    context = {
        'allmusic':allmusic
    }
    return render(req,'artistpage.html',context)
def addmusic(req):
    user = User.objects.get(id = req.session['user']['id'])
    song_title = req.POST['songtitle']
    song_writer  = req.POST['songwriter']
    song_composer = req.POST['songcomposer']
    mp3file = req.FILES['songmp3']
    duration = 3
    Music.objects.create(song_name = song_title , writer = song_writer ,composer = song_composer , duration = duration , music = mp3file , uploaded_by = user  )
    return redirect('/artistprofile')
def songpage(req):
    allmusic = Music.objects.all
    context = {
        'allmusic':allmusic
        }
    return render(req,'songpage.html',context)
def logout(req):
    req.session.clear()
    return redirect('/')
def delete(req,id):
    song = Music.objects.get(id=id)
    song.delete()
    return redirect('/artistprofile')
