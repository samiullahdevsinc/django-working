from django.contrib import admin
from django.urls import path
from .views import postCreate, loginUser, contact
from .views import postList
urlpatterns = [
    path('contact',contact,name="Contact Page"),
    path('post',postCreate,name="Post Create"),
    path('loginuser',loginUser, name="Login User"),
    path("posts", postList.as_view(),name="Post List")
]
