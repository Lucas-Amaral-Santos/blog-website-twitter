from django.test import TestCase
from news.models import Category, News
from django.contrib.auth.models import User


class TestModels(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='admin',
            password= 'admin'
        )
        self.category1 = Category.objects.create(
            name = 'Sports',
        )
        self.news1 = News.objects.create(
            title = 'Breaking News',
            body = 'body from news',
            author = self.user,
            publish = True,
            category = self.category1,
        )

    def test_news_slug_creation(self):
        self.assertEquals(self.news1.slug, 'breaking-news')

        