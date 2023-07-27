from django.urls import path, re_path
from .views import home, data, form, courses


urlpatterns = [
    path('app/', home, name="home"),
    path('data/',data, name="data"),
    path('form/',form,name="Form"),
    path('list/', courses.as_view(),name="courses"),
    re_path(r'^/id/(?p<id>\d+)$',)
]