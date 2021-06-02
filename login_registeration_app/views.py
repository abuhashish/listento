from django.shortcuts import redirect, render,HttpResponse

# Create your views here.
def root(request):
    return redirect('/login')
def login (request):
    return render(request,"login.html")
def register(request):
    return HttpResponse('hello')

    
