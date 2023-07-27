from django.contrib import admin
from .models import User,Admin, Student, Courses, username, userProfile
# Register your models here.
admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Student)
admin.site.register(Courses)
admin.site.register(username)
admin.site.register(userProfile)
