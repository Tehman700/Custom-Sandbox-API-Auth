from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins, generics
from .models import *
from .serializers import *

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.



def registerView(request):
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if User.objects.filter(username = username).exists():
            return HttpResponse("THis user already exists")
        
        user = User.objects.create(username = username, password = password)
        
        return HttpResponse("User Created Successfully")
        
    return render(request, 'register.html')


    
    


def loginView(request):
    
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username = username , password = password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("User invalid Successfully")
        
    
    return render(request, 'login.html')





@login_required(login_url='/login/')
def homeView(request):
    return render(request, 'home.html')