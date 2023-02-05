from django.shortcuts import render
from .models import Post

# Create your views here.

def articl_list(request):
    articles=Post.objects.all().order_by
    return render (request,'blog/article_list.html',{'articles':articles})

