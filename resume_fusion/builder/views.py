from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse
from django.template import loader

def members(request):
    return HttpResponse("Hello World!")

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'builder/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'builder/register.html', {'form': form})

def dashboard(request):
    template = loader.get_template('builder/dashboard.html')
    return HttpResponse(template.render())

def master(request):
    template = loader.get_template('builder/base.html')
    return HttpResponse(template.render())

def forms(request):
    template = loader.get_template('builder/data_forms.html')
    return HttpResponse(template.render())

def design(request):
    template = loader.get_template('builder/customize.html')
    return HttpResponse(template.render())

def download(request):
    template = loader.get_template('builder/download.html')
    return HttpResponse(template.render())