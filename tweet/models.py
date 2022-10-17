from django.db import models

# Create your models here.

class TweetModel(models.Model):
    class Meta:
        db_table = 'tweet_table'

    img_upload = models.ImageField(upload_to='tweet', null=True)
    img_upload_log = models.ImageField(upload_to='tweet')
    img_category = models.CharField(max_length=256)
