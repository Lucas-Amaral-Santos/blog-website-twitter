from django.shortcuts import render, redirect

from news.models import News

def home(request):
    if not request.user.is_authenticated:
        return redirect('/signin/')

    news = News.published.all()

    return render(request, 'home.html', {'news': news})


def about(request):
    if not request.user.is_authenticated:
        return redirect('/signin/')

    return render(request, 'about.html', {})


def contact(request):
    if not request.user.is_authenticated:
        return redirect('/signin/')

    return render(request, 'contact.html', {})