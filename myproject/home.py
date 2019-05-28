from django.shortcuts import render

def login(request):
    return render (request,'home.html')

def homepage(request):
    return render(request, 'homepage.html')

def register(request):
    return render(request, 'register.html')