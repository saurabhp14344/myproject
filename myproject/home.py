from django.shortcuts import render
from django.http import *
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('homepage')
    return render(request, 'login.html')

def homepage(request):
    return render(request, 'homepage.html')

