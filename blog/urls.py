from django.urls import path
from .views import ArticleList,ArticleDetail#article_list

urlpatterns=[
    # path('list',articl_list)
    path('list',ArticleList.as_view()), 
    path('detail/<slug:slug>',ArticleDetail.as_view(),name='detail'),
]