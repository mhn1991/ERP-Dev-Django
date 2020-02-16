from django.contrib.auth import authenticate , login
from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
def showLogin(request, *args,**kwargs):
    return render(request, "login.html",{})

def checkLogin(request, *args,**kwargs):
    if request.method == 'POST':
        user = request.POST['username']
        password = request.POST['password']
        auth = authenticate(request,username=user, password=password)
        if auth is not None:
            login(request, auth)
            return HttpResponseRedirect('/dashboard/')
        else:
            return HttpResponseRedirect('/login/')
