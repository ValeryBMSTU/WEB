from django.conf.urls import url, include
from django.urls import path
from .views  import *
from .models import *
from django.views.generic import ListView, DetailView 

urlpatterns = [
    path('index/', index, name="index"),
    path('tag/', tag, name="tag"),
    path('ask/', ask, name="ask"),
    path('question/', question, name="question"),
    path('settings/', settings, name="settings"),
    path('login/', login, name="login"),
    path('registration/', registration, name="registration"),
    path('users/', users, name="users"),
    path('questionsByDate/', QuestionByDateView.as_view(), name='questionsByDate'),
    path('questionsByRate/', QuestionByRateView.as_view(), name='questionsByRate'),
    path('questionsByTag/', QuestionByTagView.as_view(), name='questionsByTag'),
    path('questions/<int:number>/', questions_detail, name='question_detail'),
    path('questions/', ListView.as_view(queryset=Question.objects.all().order_by("title")[:10], template_name="asker/questions.html")),
]