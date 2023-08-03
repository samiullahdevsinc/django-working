from django.test import TestCase
from .models import Post

# Create your tests here.

# class URLTests(TestCase):

# 	def test_homepage(self):
# 		response = self.client.post('/posts')
# 		self.assertEqual(response.status_code,200)


class MODELTests(TestCase):
    def test_model_post(self):
        title = Post.objects.create(title="Django Testing")
        # You should only create the "title" object for testing the model.

        # Correct assertion by retrieving the "title" from the database.
        retrieved_title = Post.objects.get(title="Django Testing")
        self.assertEqual(retrieved_title.title, "Django Testing")
