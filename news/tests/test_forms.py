from django.test import TestCase
from django.contrib.auth.models import User
from news.forms import CategoryForm, NewsForm
from news.models import Category


class TestForms(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='admin',
            password= 'admin'
        )
        self.category = Category.objects.create(
            name = 'Sports',
        )

    def test_category_form_valid(self):
        form_category = CategoryForm(data={
            'name': 'Politics',
        })

        self.assertTrue(form_category.is_valid())

    def test_category_form_invalid(self):
        form_category = CategoryForm(data={})

        self.assertFalse(form_category.is_valid())
        self.assertEquals(len(form_category.errors), 1)


    def test_news_form_valid(self):
        form_news = NewsForm(data={
            'title': 'news2',
            'body': "body from news",
            'author': 1,
            'category': 1,
            'publish': True,
        })

        self.assertTrue(form_news.is_valid())

    def test_news_form_invalid(self):
        form_news = NewsForm(data={})

        self.assertFalse(form_news.is_valid())
        self.assertEquals(len(form_news.errors), 4)