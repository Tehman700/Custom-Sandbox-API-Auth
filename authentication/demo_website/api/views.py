from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
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

from django.contrib import messages
# Create your views here.



def registerView(request):


    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})



def loginView(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():

            user = form.get_user()
            login(request, user)
            return redirect('dashboard')


    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})



@login_required
def dashboard(request):
    messages = AdminMessage.objects.all().order_by('-uploaded_at')
    return render(request, 'dashboard.html', {'messages': messages})

def logout_view(request):
    logout(request)
    return redirect('logins')













# Static admin credentials
ADMIN_USERNAME = 'admin123'
ADMIN_PASSWORD = 'securepass'

def admin_panel(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            request.session['is_admin'] = True  # store admin login in session
            return redirect('admin_dashboard')
        else:
            messages.error(request, "Invalid admin credentials.")

    return render(request, 'admin_panel.html')


def admin_dashboard(request):
    if not request.session.get('is_admin'):
        return redirect('admin_panel')

    if request.method == 'POST':
        text = request.POST.get('message')
        if text:
            AdminMessage.objects.create(message=text)

    messages = AdminMessage.objects.all().order_by('-uploaded_at')

    return render(request, 'admin_dashboard.html', {'messages': messages})