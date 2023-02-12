from django.shortcuts import render,get_object_or_404
from .models import Post
from django.views.generic import ListView,DetailView

# Create your views here.

# def article_list(request):
#     articles=Post.objects.all().order_by('created')
#     return render (request,'blog/article_list.html',{'articles':articles})

class ArticleList(ListView):
    queryset=Post.objects.all()
    template_name='blog/article_list.html'
    paginate_by = 5     

class ArticleDetail(DetailView):
    template_name='blog/article_detail.html'
    def get_object(self):
        slug=self.kwargs.get('slug')
        return get_object_or_404(Post.objects.all(),slug=slug)
        # Post.objects.get(slug=slug)