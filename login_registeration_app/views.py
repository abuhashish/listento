from django.shortcuts import render

def Homepage(req):
    return render(req,'login.html')
