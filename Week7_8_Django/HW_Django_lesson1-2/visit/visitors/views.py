from django.urls import reverse

from visitors.forms import NewVisitorForm
from .models import Visitor
from django.views.generic import ListView, DetailView, CreateView


class VisitorListView(ListView):
    model = Visitor
    template_name = "index.html"


class VisitorDetailView(DetailView):
    model = Visitor
    template_name = "detail.html"


class VisitorAddView(CreateView):
    model = Visitor
    template_name = "add_visitor.html"
    form_class = NewVisitorForm

    def get_success_url(self):
        return reverse('detail', args=(self.object.id,))
