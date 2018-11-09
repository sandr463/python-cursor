from django.http import HttpResponse
from .models import Article
from django.shortcuts import render, get_object_or_404, redirect
from .forms import NewArticleForm
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse


class IndexView(ListView):
    model = Article
    template_name = "index.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data()
        context['page_title'] = 'All articles'
        return context



class ArticleDetailView(DetailView):
    model = Article
    template_name = "detail.html"


class ArticleCreateView(CreateView):
    model = Article
    template_name = "add_article.html"
    form_class = NewArticleForm

    def get_success_url(self):
        return reverse('detail', args=(self.object.id,))