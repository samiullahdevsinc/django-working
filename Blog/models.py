from django.db import models
import uuid
# Create your models here.
class User(models.Model):
	fullName = models.CharField(max_length=300, null=True)
	email = models.EmailField()
	PhoneNumber = models.CharField(max_length=200)
	password = models.CharField(max_length=30)

	class Meta:
		verbose_name="stu"

	def __str__(self):
		return self.email

class Admin(models.Model):
	User= models.OneToOneField(User, default=None,null=True,on_delete=models.CASCADE)
	genderChoice = [('M',"Male"),('F',"Female")]
	gender = models.CharField(max_length=6,choices = genderChoice)

	

class Post(models.Model):
	title = models.CharField(max_length=50,verbose_name="Title Mine")
	detail = models.TextField()
	User= models.ForeignKey(User,default=None, null=True, on_delete=models.CASCADE)
	likes = models.IntegerField()

	def __str__(self):
		return self.title

# Post.objects.filter(Q(title="Sami") | Q(title="Toheed"))

class Comment(models.Model):
	user = models.ForeignKey(User, default=None,null=True,on_delete=models.CASCADE)
	post = models.ForeignKey(Post, default=None,null=True,on_delete=models.CASCADE)
	comment = models.CharField(max_length=300)
	like = models.IntegerField()

