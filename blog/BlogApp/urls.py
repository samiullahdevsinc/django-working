from django.contrib import admin
from django.urls import path
from .views import postCreate, loginUser
from .views import postList
urlpatterns = [
    path('post',postCreate,name="Post Create"),
    path('loginuser',loginUser, name="Login User"),
    path("posts", postList.as_view(),name="Post List")
]
