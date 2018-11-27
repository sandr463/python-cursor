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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from visitors.views import VisitorListView, VisitorDetailView, VisitorAddView, LoginFormView, LogoutFormView, \
    VisitorUpdateView, VisitorDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', VisitorListView.as_view(), name='index'),
    path('visitor/<int:pk>', VisitorDetailView.as_view(), name='detail'),
    path('add_visitor', VisitorAddView.as_view(), name='add_visitor'),
    path('visitor/update/<int:pk>', VisitorUpdateView.as_view(), name='update_visitor'),
    path('visitor/delete/<int:pk>', VisitorDeleteView.as_view(), name='delete_visitor'),

    path('login', LoginFormView.as_view(), name='login'),
    path('logout', LogoutFormView.as_view(), name='logout'),

    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
