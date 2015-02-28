from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .models import Task

def index(request):
    return render(request, 'index.html', {})

def profile(request):
    tasks = Task.objects.all()
    return render(request, 'profile.html', {
        'tasks': tasks
    })

def about(request):
    return render(request, 'about.html', {})
