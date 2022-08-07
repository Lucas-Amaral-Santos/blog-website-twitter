from turtle import title
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                    self).get_queryset()\
                    .filter(publish=True)

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='news_user')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='news_category')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=250)
    publish = models.BooleanField()
    objects = models.Manager()

    published = PublishedManager()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.id)
        super(News, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title