from django.urls import reverse
from visitors.forms import NewVisitorForm
from .models import Visitor
from django.views.generic import ListView, DetailView, CreateView, FormView, View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect


class VisitorListView(ListView):
    model = Visitor
    template_name = "index.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(VisitorListView, self).get_context_data()
        context['page_title'] = 'All visitors'
        return context


class VisitorDetailView(DetailView):
    model = Visitor
    template_name = "detail.html"


class VisitorAddView(CreateView):
    model = Visitor
    template_name = "add_visitor.html"
    form_class = NewVisitorForm

    def get_success_url(self):
        return reverse('detail', args=(self.object.id,))


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url = '/'

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutFormView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('login')
