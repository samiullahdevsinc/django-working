from django.contrib import admin
from .models import User,Admin,Post,Comment
# Register your models here.
admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Post)
admin.site.register(Comment)