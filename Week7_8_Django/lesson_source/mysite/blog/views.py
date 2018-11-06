from django.http import HttpResponse
from .models import Article
from django.shortcuts import render, get_object_or_404


def index(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {'articles': articles})

def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'detail.html', {'article': article})

def add_article(request):
    if request.POST:
        Article.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            author=request.POST.get('author')
        )
        print('======================')
        print(request.POST)
    return render(request, 'add_article.html')