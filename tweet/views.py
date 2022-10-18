from django.shortcuts import render, redirect
from . import tests
from django.contrib.auth import authenticate
from .models import TweetModel

# Create your views here.

def home(request):
    if request.method == 'GET': 
        user = request.user.is_authenticated
        if user:
            # 추가할 것 : 업로드한 이미지 보여주기(view_img), 이미지를 인식한 카테고리(img_catagory) 
            temp = TweetModel.objects.values('upload_img')
            print(temp)
        
            # all_upload_img = [x['upload_img'] for x in temp]
            
            # return render(request, 'tweet/home.html', {'upload_img': all_upload_img})
            return render(request, 'tweet/home.html', {'upload_img':temp})
        else:
            return redirect('/login')
            
    elif request.method == 'POST':
        user = request.user.is_authenticated
        tweet = TweetModel()

        upload_img = request.FILES['upload_img']

        tweet.upload_img = upload_img
        # tweet.category = 1
        # tweet.upload_label_img = 2

        tweet.save()
        
        # img_data = {
        #     'img_log':tweet.img_log,
            
        # }
        return render(request, 'tweet/home.html')
        # https://stackoverflow.com/questions/64002542/how-to-use-yolov5-model-in-django   -> stackoverflow django,yolov5 연동하는 코드