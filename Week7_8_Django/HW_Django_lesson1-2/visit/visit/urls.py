"""visit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from visitors.views import VisitorListView, VisitorDetailView, VisitorAddView, LoginFormView, LogoutFormView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', VisitorListView.as_view(), name='index'),
    path('visitor/<int:pk>', VisitorDetailView.as_view(), name='detail'),
    path('add_visitor', VisitorAddView.as_view(), name='add_visitor'),

    path('login', LoginFormView.as_view(), name='login'),
    path('logout', LogoutFormView.as_view(), name='logout'),
]
