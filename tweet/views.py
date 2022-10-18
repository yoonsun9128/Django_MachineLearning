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
            temp2 = TweetModel.objects.values('upload_label_img')
            result = zip(temp, temp2)
            print(temp)
        
            # all_upload_img = [x['upload_img'] for x in temp]
            
            # return render(request, 'tweet/home.html', {'upload_img': all_upload_img})
            return render(request, 'tweet/home.html', {'total_img':result})
        else:
            return redirect('/login')
            
    elif request.method == 'POST':
        user = request.user.is_authenticated
        tweet = TweetModel()

        upload_img = request.FILES['upload_img']

        tweet.upload_img = upload_img
        tweet.save()

        tweet = TweetModel.objects.get(upload_img=f'images/{upload_img}')

        upload_label_img, category = tests.change_img(upload_img)
        
        tweet.category = category
        tweet.upload_label_img = upload_label_img
        tweet.save()
        
        return redirect('/')
