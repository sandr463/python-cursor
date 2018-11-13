from .models import Article
from django.shortcuts import render


def index(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {'articles': articles})


def detail(request, id_article):
    article = Article.objects.get(id=id_article)
    return render(request, 'detail.html', {'article': article})
