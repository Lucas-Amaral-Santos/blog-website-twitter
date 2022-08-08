from django.test import TestCase, Client
from django.urls import reverse
from news.models import Category, News
from django.contrib.auth.models import User
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.submit_news_url = reverse('news:submit_news')
        self.submit_category_url = reverse('news:submit_category')
        self.user = User.objects.create(
            username='admin',
            password= 'admin'
        )
        self.category1 = Category.objects.create(
            name = 'Sports',
        )
        self.news1 = News.objects.create(
            title = 'news1',
            body = 'body from news',
            author = self.user,
            publish = True,
            category = self.category1,
        )
    
    def test_submit_news_GET(self):
        response = self.client.get(self.submit_news_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'submit_news.html')

    def test_submit_category_GET(self):
        response = self.client.get(self.submit_category_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'submit_category.html')

    def test_submit_news_POST(self):
        response = self.client.post(self.submit_news_url, {
            'title': 'news2',
            'body': 'body from news',
            'author': self.user,
            'publish': True,
            'category': self.category1,
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.news1.title, 'news1')

    def test_submit_category_POST(self):
        response = self.client.post(self.submit_category_url, {
        'name': 'Romance',
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.category1.name, 'Sports')