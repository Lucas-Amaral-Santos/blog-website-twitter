from django import forms
from .models import News, Category

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title','body','author', 'category', 'publish']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'