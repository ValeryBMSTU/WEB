from django.conf.urls import url, include
from django.urls import path
from django.views.generic import ListView, DetailView
from asker.models import Ask, Question, Tag
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('tag/', views.tag, name="tag"),
    path('ask/', views.ask, name="ask"),
    path('question/', views.question, name="question"),
    path('settings/', views.settings, name="settings"),
    path('login/', views.login, name="login"),
    path('registration/', views.registration, name="registration"),
    #path('asks/', ListView.as_view(queryset=Asks.objects.all().order_by("Title")[:20], template_name="asker/asks.html"))
]