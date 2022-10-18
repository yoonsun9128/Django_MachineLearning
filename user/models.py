from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class UserModel(AbstractUser):
    class Meta:
        db_table = 'user_table'

    nickname = models.CharField(max_length=10, null=True ,unique=True, blank=False)