from django.http import request
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
    all_artists = User.objects.filter(role=1)
    contixt = {
        'all_artists':all_artists
    }
    return render(request,'artistspage.html',contixt)
def userprofile(req):
    user = User.objects.get(id=req.session['user']['id'])
    allmusic = Music.objects.all
    context={
        'x': user,
        'allmusic':allmusic
    }
    if user.role == Role.objects.get(id=2):
        return render(req,'userprofile.html',context)
    return render(req,'artistpage.html',context)
def artistprofile(req,id):
    user = User.objects.get(id=id)
    allmusic = Music.objects.all
    allmusic = Music.objects.all
    context = {
        'x': user,
        'allmusic':allmusic
    }
    return render(req,'artistpage.html',context)
def addmusic(req,id):
    user = User.objects.get(id = id)
    song_title = req.POST['songtitle']
    song_writer  = req.POST['songwriter']
    song_composer = req.POST['songcomposer']
    mp3file = req.FILES['songmp3']
    duration = 3
    Music.objects.create(song_name = song_title , writer = song_writer ,composer = song_composer , duration = duration , music = mp3file , uploaded_by = user  )
    return redirect('/artistprofile/'+str(id))
def songpage(req,id):
    allmusic = Music.objects.filter(id=id)
    context = {
        'allmusic':allmusic,

        }
    return render(req,'songpage.html',context)
def logout(req):
    req.session.clear()
    return redirect('/')
def delete(req,id):
    song = Music.objects.get(id=id)
    song.delete()
    return redirect('/artistprofile/'+str(req.session['user']['id']))
def requesttobeartist(req):
    user = User.objects.get(id = req.session['user']['id'])
    if user.role == Role.objects.get(id=2):
        user.role = Role.objects.get(id=1)
        user.save()
        return redirect('/userprofile')
    user.role = Role.objects.get(id=2)
    user.save()
    return redirect('/userprofile')

def admin(req):
    if 'user' in req.session:
        if 'role' in req.session['user']:
            context= {
                            'user' : User.objects.get(id=req.session['user']['id']),
                            
                        }
            return render(req,'admin.html',context)
    else:
        return render(req,"adminlogin.html")
def adminhandle(req):
    if req.method == "GET":
        return redirect('/admin')
    if req.method == "POST":
        user = User.objects.filter(username = req.POST['user'])
        psswd = req.POST['pass'] 
        if user:
            logged_user=user[0]
            if logged_user.role.role=="admin":
                if bcrypt.checkpw(psswd.encode(), logged_user.password.encode()):
                    req.session['user']={
                        'fname':logged_user.first_name,
                        'lname':logged_user.last_name,
                        'id':logged_user.id,
                        'role':logged_user.role.role,
                        
                    }
                    context= {
                        'user' : User.objects.get(id=req.session['user']['id']),
                        
                    }
                return render(req,'admin.html',context)
            return redirect('/admin')
    else:
        return('/home')
def adminprofile(req):
    user=User.objects.get(id=req.session['user']['id'])
    context={
        'user':user
    }
    return render(req,"adminprofile.html")
def artistrequest(req):
    user=User.objects.get(id=req.session['user']['id'])
    if user.role.role == "admin":
        all=LOL.objects.all()
        context={
            'all':all,
            'user':user
        }
    return render(req,"artistrequest.html",context)