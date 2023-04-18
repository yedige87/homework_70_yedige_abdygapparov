"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include

from api.views import TasksAPIView, DetailView, UpdateView, DeleteView, CreateView, ProjectsAPIView, ProjectDetailView, \
    ProjectUpdateView, ProjectCreateView, ProjectDeleteView, TypesAPIView, TypeDetailView, TypeUpdateView, \
    TypeCreateView, TypeDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webapp.urls')),
    path('api/tasks', TasksAPIView.as_view()),
    path('api/tasks/<int:pk>', DetailView.as_view()),
    path('api/tasks/<int:pk>/update', UpdateView.as_view()),
    path('api/tasks//create', CreateView.as_view()),
    path('api/tasks/<int:pk>/delete', DeleteView.as_view()),
    path('api/projects', ProjectsAPIView.as_view()),
    path('api/projects/<int:pk>', ProjectDetailView.as_view()),
    path('api/projects/<int:pk>/update', ProjectUpdateView.as_view()),
    path('api/projects//create', ProjectCreateView.as_view()),
    path('api/projects/<int:pk>/delete', ProjectDeleteView.as_view()),
    path('api/types', TypesAPIView.as_view()),
    path('api/types/<int:pk>', TypeDetailView.as_view()),
    path('api/types/<int:pk>/update', TypeUpdateView.as_view()),
    path('api/types//create', TypeCreateView.as_view()),
    path('api/types/<int:pk>/delete', TypeDeleteView.as_view()),
    path('auth/', include('accounts.urls')),
]