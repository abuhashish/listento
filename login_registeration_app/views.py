from django.shortcuts import redirect, render,HttpResponse

# Create your views here.
def root(request):
    print(5)
    return redirect('/login')
def login (request):
    print(5)
    return render(request,"login.html")
def register(request):
    return render(request,'registeration.html')
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
