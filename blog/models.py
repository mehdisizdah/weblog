from django.db import models
from account.models import User
from django.utils import timezone
# from datetime import datetime

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    author=models.ForeignKey(User,on_delete=models.PROTECT)
    created=models.DateTimeField(auto_now_add=True )
    updated=models.DateTimeField(auto_now=True)
    publish=models.DateTimeField(default=timezone.now)
    slug=models.SlugField(max_length=100 )
    image=models.ImageField()
    
    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.description[:30]+'...'