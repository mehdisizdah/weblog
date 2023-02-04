from django.db import models
from account.models import User

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=100)
    desctiption=models.TextField()
    author=models.ForeignKey(User,on_delete=models.PROTECT)