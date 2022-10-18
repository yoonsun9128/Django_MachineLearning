from django.db import models

# Create your models here.

class TweetModel(models.Model):
    class Meta:
        db_table = 'tweet_table'

    upload_img = models.ImageField(upload_to='images/', null=True)
    upload_label_img = models.ImageField(upload_to='images/')
    category = models.CharField(max_length=256)
