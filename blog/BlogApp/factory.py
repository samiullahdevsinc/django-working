import factory
from django.contrib.auth.models import User
from .models import Post

from factory.faker import faker

Fake = faker.Faker()


class PostFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Post

	title = factory.Faker("sentence",nb_words=12)
	details = Fake.paragraph(nb_sentences=40)
	title1 = factory.Faker("sentence",nb_words=20)
	# slug = fackory.Faker("slug")
	# author = User.objects.get_or_create(username="admin")[0]


x = PostFactory.create_batch(100)