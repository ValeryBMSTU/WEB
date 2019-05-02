from django.urls import path
from .views import *

urlpatterns = [
    path('', newQuestions, name="NewQuestions"),
    path('questions/', questions, name="Questions"),
    path('questions/hot/', hotQuestions, name='HotQuestions'),
    path('questions/<int:pk>/', questionDetail, name='QuestionDetail'),
    path('tags/', tags, name='Tags'),
    path('tags/<str:slug>/', tagDetail, name="TagDetail"),
    path('ask/', ask, name="Ask"),
    path('settings/', settings, name="Settings"),
    path('login/', login, name="login"),
    path('registration/', registration, name="Registration"),
    path('users/', users, name="Users"),

    # path('login_sem/', login, name="login"),
]