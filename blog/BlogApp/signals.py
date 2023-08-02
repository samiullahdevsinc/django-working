# signals.py
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Post

@receiver(post_save, sender=Post)
def save_post(sender, instance, **kwargs):
    print("Save Signal is Calling")


@receiver(post_delete,sender=Post)
def delete_post(sender,instance,**kwargs):
	print("Delete Signal is Calling")
