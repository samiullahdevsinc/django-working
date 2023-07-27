from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm, PostForm
# Create your views here.
def checkId(request,id):
	return HttpResponse(f"The id is {id}")


def userFormView(request):
	if request.method == "POST":
		form = PostForm(request.POST)

		if form.is_valid():
			print(request.POST)
			try:
				form.save()
			except Exception as e:
				print(e)
			return HttpResponse(" Yes The Form is Valid")

	form = PostForm()
	return render(request,'userform.html',{'form':form})