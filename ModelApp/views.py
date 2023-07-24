from django.shortcuts import render
from .models import username, userProfile
from django.views.generic import ListView
# Create your views here.


def home(request):
	print("Yes, I it's calling me")
	usernames = username.objects.all()
	print(usernames)
	return render(request,"home.html")

def form(request):
	return render(request,"form.html")

def data(request):
	name = request.POST['name']
	print(name)
	return render(request,"home.html")


class courses(ListView):
	model = username
	template_name = "username_list.html"
	# fields = ['username']
	context_object_name = 'courses'
	# success_url = '/list/'




'''
A view function, or view for short, is a Python function that takes a Web request and returns a Web response.
This response can be the HTML contents of a Web page, or a redirect, or a 404 error, or an XML document, or an image . . . or anything, really. The view itself contains whatever arbitrary logic is necessary to return that response.

* Async Views:
As well as being synchronous functions, views can also be asynchronous (“async”) functions, normally defined using Python’s async def syntax.
Django will automatically detect these and run them in an async context. However, you will need to use an async server based on ASGI to get their performance benefits.

import datetime
from django.http import HttpResponse

async def current_datetime(request):
    now = datetime.datetime.now()
    html = '<html><body>It is now %s.</body></html>' % now
    return HttpResponse(html)


* There are two types of views. Class based Views and Function based veiws.
Class based views never replace function based but in larger application. Our code start repeating and overwrite DRY law.
So, we use class based views. It's totally upto you whatever view you want to use.

* Class based views have generic views.
* If you are having problem in using generic views, you can just use your own view. It will become easy for you to manage.

Example:

from django.views.generic.list import ListView
from .models import GeeksModel
 
class GeeksList(ListView):
 
    # specify the model for list view
    model = GeeksModel



Example of Class View
class courses(ListView):
	model = username
	template_name = "username_list.html"
	context_object_name = 'courses'

class courses(CreateView):
	model = username
	template_name = "username_list.html"
	fields = ['username']
	context_object_name = 'courses'
	success_url = '/list/'


'''	