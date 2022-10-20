from django.shortcuts import render, redirect
from . import function, tests
from django.contrib.auth import authenticate
from .models import TweetModel
import os
from uuid import uuid4
from Django_AI.settings import MEDIA_URL, MEDIA_ROOT

# Create your views here.

def home(request):
    """
    test <QuerySet [{'id': 10, 'upload_img': 'images/KakaoTalk_20221018_164355499.jpg', 
    'upload_label_img': 'after_imageKakaoTalk_20221018_164355499.jpg', 
    'category': "['car']"}, 
    {'id': 11, 'upload_img': 'images/gyuhyeon.jpg', 'upload_label_img': 'after_imagegyuhyeon.jpg', 'category': "['person']"}]>
    """
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
        tweet.age = temp_age
        tweet.gender = temp_gender
        tweet.save()
        # ['Female'] ['(25-32)']

        print(request.POST)
        p_class = request.POST['p_class']
        gender = 1
        if temp_gender[0] == 'Female':
            gender = 0
        fare = float(request.POST.get('fare'))
        barked = int(request.POST.get('barked'))

        age = temp_age
        band_age = 0
        
        family_size = int(request.POST.get('family_size'))
        alone = 0
        if family_size == 0:    
            alone = 1

        user_info = [[p_class, gender, fare, barked, 1, family_size, alone]]

        result = 0
        result = function.is_survived(user_info)
        
        if result == 0:
            print('주금')
        else:
            print('생존')

        return render(request, 'tweet/home.html', {'result': result}) # html 에서 result 0 이면 죽음 1이면 새


