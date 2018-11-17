from django.shortcuts import render
from .models import Visitor
from django.views.generic import ListView, DetailView, CreateView


class VisitorListView(ListView):
    model = Visitor
    template_name = "index.html"


class VisitorDetailView(DetailView):
    model = Visitor
    template_name = "detail.html"
