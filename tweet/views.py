from django.shortcuts import render, redirect
from . import function, tests
from django.contrib.auth import authenticate
from .models import TweetModel
import os
from uuid import uuid4
from Django_AI.settings import MEDIA_URL, MEDIA_ROOT
import random
import warnings
from django.contrib import auth
from django.contrib.auth.decorators import login_required
warnings.filterwarnings('ignore')

# Create your views here.

def home(request):
    if request.method == 'GET': 
        user = request.user.is_authenticated
        if user:
            return render(request, 'tweet/home.html')
        else:
            return redirect('/login')
            
    elif request.method == 'POST':
        user = request.user.is_authenticated
        tweet = TweetModel()
        upload_img = request.FILES['upload_img']
        tweet.upload_img = upload_img
        tweet.save()
        
        temp_gender, temp_age = function.photo(tweet.upload_img)
        if temp_gender == 0 and temp_age == 0:
            return render(request, 'tweet/home.html', {'result': -1})
        # ['Female'] ['(25-32)']

        name = request.POST.get('name')
        p_class = int(request.POST.get('p_class'))
        gender = 0
        if temp_gender[0] == 'Female':
            gender = 1
        fare = float(request.POST.get('fare'))
        barked = int(request.POST.get('barked'))

        age = temp_age[0][1:-1].split('-')
        random_age = random.randint(int(age[0]), int(age[1]))

        if 0 <= random_age <= 16:
            result_age = 0
        elif 16 < random_age <= 32:
            result_age = 1
        elif 32 < random_age <= 48:
            result_age = 2
        elif 48 < random_age <= 64:
            result_age = 3
        else:
            result_age = 4
        
        family_size = int(request.POST.get('family_size'))
        alone = 0
        
        if family_size == 0:    
            alone = 1
        
        user_info = [[p_class, gender, fare, barked, result_age, family_size, alone]]
        result = 0
        result = function.is_survived(user_info)
        to_result_html = {'result': result, 'name': name, 'age': random_age, 'gender': gender, 'family_size': family_size, 'p_class': p_class, 'fare': int(fare), 'images': tweet.upload_img}
        # result 0 이면 죽음 1이면 생존

        return render(request, 'tweet/result.html', {'total_data': to_result_html})

# 로그아웃 버튼
@login_required
def logout(request):
    auth.logout(request)
    return  redirect('/')