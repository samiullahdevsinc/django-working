from django.db import models

# Create your models here.

class Post(models.Model):
	pId = models.BigAutoField(primary_key=True)
	title = models.CharField(max_length=30)
	details = models.TextField()
	title1 = models.CharField(max_length=30)