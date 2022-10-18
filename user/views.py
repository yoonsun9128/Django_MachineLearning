from django.shortcuts import render, redirect
from .models import UserModel
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return redirect('user/login')
    else:
        
        return render(request, 'user/login.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'user/signup.html')

    if request.method == 'POST':
        user = UserModel()
        user.username = request.POST.get('username')
        user.set_password(request.POST.get('password'))
        user.nickname = request.POST.get('nickname')
        
        if user.username == '' or user.set_password == '':
            return render(request, 'user/signup.html')
        
        exist_user = get_user_model().objects.filter(username=user.username)
        if exist_user:
            return render(request, 'user/signup.html')
        
        user.save()
        return redirect('/login')
    
    

@login_required
def logout(request):
    auth.logout(request)
    return redirect('/login')