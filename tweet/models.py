from django.db import models
from imagekit.models import ProcessedImageField
import os
import uuid
# Create your models here.

class TweetModel(models.Model):
    class Meta:
        db_table = 'tweet_table'

    upload_img = ProcessedImageField(
        upload_to='images', 
        format='JPEG', 
        options = {'quality': 100})
    
    # photo_thumbnail = ProcessedImageField(
	# 	upload_to = 'blog/post',
	# 	processors = [Thumbnail(100, 100)], # 처리할 작업 목룍
	# 	format = 'JPEG',					# 최종 저장 포맷
	# 	options = {'quality': 60})
    # upload_label_img = models.ImageField(upload_to='images/')
    
    age =models.CharField(max_length=10)
    gender =models.CharField(max_length=10)

# https://tothefullest08.github.io/django/2019/06/04/Django17_image/
# https://iamthejiheee.tistory.com/98
# https://wayhome25.github.io/django/2017/05/11/image-thumbnail/