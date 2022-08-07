from django.urls import path
from .views import submit_news, submit_category

app_name = 'news'


urlpatterns = [
    path('submit_news/', submit_news, name='submit_news'),
    path('submit_category/', submit_category, name='submit_category'),
]
