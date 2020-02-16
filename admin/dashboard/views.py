from django.contrib.auth import authenticate
from django.shortcuts import render                                               
from django.http import HttpResponseRedirect 
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def showDashboard(request, *args,**kwargs):
    return render(request,"dashboard.html",{})
