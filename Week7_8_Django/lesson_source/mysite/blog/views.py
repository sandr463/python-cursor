from django.http import HttpResponse, HttpResponseRedirect
from .models import Article
from django.shortcuts import render, get_object_or_404, redirect
from .forms import NewArticleForm
from django.views.generic import ListView, DetailView, CreateView, FormView, View, UpdateView, DeleteView
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout


class IndexView(ListView):
    model = Article
    template_name = "index.html"


class ArticleDetailView(DetailView):
    model = Article
    template_name = "detail.html"


class ArticleCreateView(CreateView):
    model = Article
    template_name = "add_article.html"
    form_class = NewArticleForm

    def get_success_url(self):
        return reverse('detail', args=(self.object.id,))

