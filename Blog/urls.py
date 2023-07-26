from django.urls import path, re_path
from .views import checkId, userFormView



urlpatterns = [
    # path('app/', home, name="home"),
    # path('data/',data, name="data"),
    # path('form/',form,name="Form"),
    # path('list/', courses.as_view(),name="courses"),
    re_path(r'^id/(?P<id>[A-z-z0-9]+)$',checkId,name="Check Id"),
    path('form/',userFormView,name="User Form View")
]