from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
# from django.contrib.admin import ModelAdmin
# Register your models here.

admin.site.register(User,UserAdmin)