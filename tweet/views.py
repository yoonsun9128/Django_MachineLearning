from django.shortcuts import render, redirect
from . import tests
from django.contrib.auth import authenticate
from .models import TweetModel
from Django_AI.settings import MEDIA_ROOT,MEDIA_URL
# Create your views here.

def home(request):
    if request.method == 'GET': 
        user = request.user.is_authenticated
        if user:
            # 추가할 것 : 업로드한 이미지 보여주기(view_img), 이미지를 인식한 카테고리(img_catagory) 
            return render(request, 'tweet/home.html')
        else:
            return redirect('/login')
            
    elif request.method == 'POST':
        print(request.POST)
        user = request.user.is_authenticated
        tweet = TweetModel()
        img_upload = request.POST['img_upload'] #이미지 업로드 기능,
        
        img_log, img_category = tests.change_img()   

        tweet.img_upload = img_upload
        tweet.img_category = img_category
        tweet.img_log = img_log
        
        for i in range(10):
            print(img_upload, img_category, img_log)

        tweet.save()
        
        # img_data = {
        #     'img_log':tweet.img_log,
            
        # }
        return render(request, 'tweet/home.html')
        # https://stackoverflow.com/questions/64002542/how-to-use-yolov5-model-in-django   -> stackoverflow django,yolov5 연동하는 코드



