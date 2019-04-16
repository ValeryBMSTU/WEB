"""askme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url, include
from django.urls import path, re_path
from django.views.generic import ListView, DetailView
from asker.models import Answer, Question, Tag, User, Status, Category
from asker import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('tag/', views.tag, name="tag"),
    path('ask/', views.ask, name="ask"),
    path('question/', views.question, name="question"),
    path('settings/', views.settings, name="settings"),
    path('login/', views.login, name="login"),
    path('registration/', views.registration, name="registration"),
    path('admin/', admin.site.urls),
    path('users/', views.users, name="users"),
    path('questionsByDate/', views.QuestionByDateView.as_view(), name='questionsByDate'),
    path('questionsByRate/', views.QuestionByRateView.as_view(), name='questionsByRate'),
    path('questionsByTag/', views.QuestionByTagView.as_view(), name='questionsByTag'),
    #path('questions/', ListView.as_view(queryset=Question.objects.all().order_by("title")[:20], template_name="asker/questions.html"))
    #path('questionDetail/', ListView.as_view(queryset=Question.objects.all().order_by("title")[:20], template_name="asker/questions.html"))
    #path("user/<int:pk>", DetailView.as_view(model = User, template_name = "user.html"))
    #url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Question, template_name = "asker/user.html"))
]
