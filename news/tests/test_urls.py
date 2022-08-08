from django.test import SimpleTestCase
from django.urls import reverse, resolve
from news.views import submit_news, submit_category

class TestUrls(SimpleTestCase):

    def test_submit_news_is_resolved(self):
        url = reverse('news:submit_news')
        self.assertEquals(resolve(url).func, submit_news)

    def test_submit_category_is_resolved(self):
        url = reverse('news:submit_category')
        self.assertEquals(resolve(url).func, submit_category)