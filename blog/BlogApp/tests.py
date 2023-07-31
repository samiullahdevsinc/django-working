from django.test import TestCase
from .models import Post

# Create your tests here.

class URLTests(TestCase):

	def test_homepage(self):
		response = self.client.post('/posts')
		self.assertEqual(response.status_code,200)


class MODELSTests(TestCase):

	def model_post(self):
		title = Post.objects.create(title="Django Testing")
		details = Post.objects.create(details="The content has been created")
		title1 = Post.objects.create(title1="The content has been created")
		self.assertEqual(str(title),"Django Testing")
		# self.assertEqual(str(details),"The content has been created")
		# self.assertEqual(str(details1),"The content has been created")
