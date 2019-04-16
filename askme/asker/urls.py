from django.conf.urls import url, include
from django.urls import path, re_path
from asker.views import questions_detail
from django.views.generic import ListView, DetailView
from asker.models import Answer, Question, Tag, User, Status, Category 
from . import views

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
    path('questions/', ListView.as_view(queryset=Question.objects.all().order_by("title")[:10], template_name="asker/questions.html"))
    #path("user/<int:pk>", DetailView.as_view(model = User, template_name = "user.html"))
    path('questions/<int:number>/', question_detail, name='question_detail'),
]