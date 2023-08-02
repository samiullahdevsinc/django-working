from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.


def contact(request):
	if request.method == "GET":
		return render(request,"contact.html")
	try:
		subject = request.POST["subject"]
		message = request.POST["message"]
		send_mail(
	    subject,
	    message,
	    'samiullah1701734@gmail.com',
	    ['azfar.intern@devsinc.com','samiullah1701734@gmail.com','obadah.intern@devsinc.com'],
	    fail_silently=False,
	)
		return HttpResponse("Email has been sent")
	except Exception as e:
		return HttpResponse(e)


@login_required(login_url="/loginuser", redirect_field_name="next")
def postCreate(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,"Post Successful created")
			form = PostForm()
		else:
			messages.info(request,"Form Invalid")
	else:
		form = PostForm()
	return render(request,"postcreate.html",{"form":form})

def loginUser(request):
	print("yes")
	if request.method == "POST":
		user = authenticate(username=request.POST["username"], password=request.POST["password"])
		if user is not None:
			login(request,user)
			return redirect("/post")
		else:
			return HttpResponse("Login Failed")
	return render(request,"login.html")

class postList(ListView):
	if User.is_authenticated:
		model = Post
		template_name = "posts.html"
		context_object_name = "posts"
		login_url = "/loginuser/"
		redirect_field_name = "next"
