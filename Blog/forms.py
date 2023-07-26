from django import forms
from .models import Post, Admin
class UserForm(forms.Form):
	fullName = forms.CharField(max_length=100,label="Full Name")
	email = forms.EmailField(required=True)
	password = forms.CharField(required=True)


class PostForm(forms.ModelForm):
	class Meta:
		model = Admin
		fields = "__all__"















'''
Unless you’re planning to build websites and applications that do nothing but publish content, and don’t accept input from your visitors, you’re going to need to understand and use forms.

Django provides a range of tools and libraries to help you build forms to accept input from site visitors, and then process and respond to the input.

Bound and unbound form instances¶

The distinction between Bound and unbound forms is important:

    * An unbound form has no data associated with it. When rendered to the user, it will be empty or will contain default values.
    * A bound form has submitted data, and hence can be used to tell if that data is valid. If an invalid bound form is rendered, it can include inline error messages telling the user what data to correct.

The form’s is_bound attribute will tell you whether a form has data bound to it or not.




* Creating Form From Model

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = "__all__"

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ["title","detail"]




'''

