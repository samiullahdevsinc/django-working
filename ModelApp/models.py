from django.db import models
import uuid
# Create your models here.

'''

1. Difference Between Null and Blank

The null option is used to specify whether the database column associated with the field should allow NULL values.
When null=True is set for a field, it means that the field can store a database NULL value, which indicates the absence of a value. 

The blank option is used to determine whether a field is required in forms. 
When blank=True is set for a field, it means that the field is not required to have a value when the model is validated through a form

Here's a summary of their differences:

    null: Specifies whether the database column allows NULL values.
    blank: Specifies whether the field is required in forms.

2. For one to Many field we use foreign key 






'''

class User(models.Model):
	id = models.BigAutoField(primary_key=True) # We are defining Custom Primary Key 
	gender = [('M','Male'),('F','Female')] # Choices Gender
	first_name = models.CharField(max_length=300)
	last_name = models.CharField(max_length=300)
	currentDate = models.DateField()
	age = models.IntegerField(blank = True, null = True)
	gender = models.CharField(max_length=300,choices = gender) # We can assign gender in choices

	def __str__(self):
		return self.first_name

	class Meta:
		pass



class Admin(models.Model):
	uuid = models.UUIDField(default = uuid.uuid4)
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	adminValue = models.BooleanField(blank=True, null=True)
	profilePhoto = models.ImageField(default=None) # Image Field 


'''

ManyToManyField()

'''

class Student(models.Model):
	courses =  models.ManyToManyField('Courses', verbose_name="Student Verbose")


class Courses(models.Model):
	name = models.CharField(max_length=100, verbose_name="Course Name")

'''

One-To-One Field

'''
class userProfile(models.Model):
	bio = models.CharField(max_length=300)
	user = models.OneToOneField('username', on_delete=models.CASCADE)
	def __str__(self):
		return self.user

class username(models.Model):
	username = models.CharField(max_length=20, unique = True)
	def __str__(self):
		return self.username



'''

Custom Field Messages

'''

class PhoneNumber(models.Model):
	def __init__(self,*args,**kwargs):
		kwargs['max_length'] = 13
		super().__init__(*args,**kwargs)

	def to_python(self,value):
		return value.replace('-','')

'''

Example to create an Object with one to one fields

user1 = username(username="Sami Ullah Saleem")
user1.save()
userprofile = userProfile(user=user1,bio="I am IT Expert")
userprofile.save()
print(userprofile)

'''

'''
ORM means Object Relational Mapper makes our life easier by making for us to shorten our query.
Like if we want to match name we can simply use it like this
Author.objects.filter(name__contains="Vic")

* __ means it's going to match things up
* 

* ORM is an acronym for the object-relational mapper. 
* The ORM’s main goal is to transmit data between a relational database and application model. The ORM automates this transmission, such that the developer need not write any SQL.

* A Queryset is a list of objects of a model. We use Querysets to filter and arrange our data.
These make our work as a Python developer easier

* In summary, select_related is used for fetching data from ForeignKey and OneToOneField relationships, 
while prefetch_related is used for ManyToManyField and reverse ForeignKey relationships.

select_related and prefetch_related short your number of queries

Example of select_related:

# Fetch all posts with their corresponding authors using select_related
posts_with_authors = Post.objects.select_related('author').all()

Example of prefetch_related
tags_with_posts = Tag.objects.prefetch_related('posts').all()

1. Django ORM is not as much as efficient as SQLAlchemy
2. Django ORM is an abstraction layer. It provides us with features like Querysets and migrations and these relations.


* In Django ORM, Q objects allow you to build complex database queries using logical operators like AND, OR, and NOT. 
They are especially useful when you need to perform complex lookups with multiple conditions. 

* Migrations are Django’s way of propagating changes you make to your models (adding a field,
deleting a model, etc.) into your database schema. They’re designed to be mostly automatic,
but you’ll need to know when to make migrations, when to run them, and the common problems


* Transactions

On databases that support DDL transactions (SQLite and PostgreSQL), all migration operations will run inside a single transaction by default. In contrast, if a database doesn’t support DDL transactions (e.g. MySQL, Oracle) then all operations will run without a transaction.

You can prevent a migration from running in a transaction by setting the atomic attribute to False. For example:

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False





'''




