from django.conf.urls import url, include
from django.urls import path
from django.views.generic import ListView, DetailView
from asker.models import Users
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('tag/', views.tag, name="tag"),
    path('ask/', views.ask, name="ask"),
    path('question/', views.question, name="question"),
    path('settings/', views.settings, name="settings"),
    path('login/', views.login, name="login"),
    path('registration/', views.registration, name="registration"),
    path('debug/', ListView.as_view(queryset=Users.objects.all().order_by("NickName")[:20], template_name="asker/users.html"))
]