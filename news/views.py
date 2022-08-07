from django.shortcuts import render, redirect
from .forms import NewsForm, CategoryForm
from .models import News, Category
from django.core.cache import cache
from django.core.mail import EmailMessage

def send_email(request, author_email):
    msg = EmailMessage('Congrats! New Article',
                       'You just submitted a new article at your blog!', to=[author_email])
    msg.send()
    return redirect('/')



# Create your views here.
def submit_news(request):
    form = NewsForm()

    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            newNews = News.objects.create(
                title = form.cleaned_data['title'],
                body = form.cleaned_data['body'],
                author = form.cleaned_data['author'],
                publish = form.cleaned_data['publish'],
                category = form.cleaned_data['category'],
            )

            newNews.save()
            print(request.user.email)
            send_email(request, request.user.email)
            cache.clear()
        return redirect('/')
    return render(request, 'submit_news.html', {'form':form})


def submit_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            newCategory = Category.objects.create(
                name = form.cleaned_data['name'],
            )

            newCategory.save()
            cache.clear()
        return redirect('/')
    return render(request, 'submit_category.html', {'form':form})