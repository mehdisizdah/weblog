from django.urls import path
from .views import articl_list

urlpatterns=[
    path('list',articl_list)
]