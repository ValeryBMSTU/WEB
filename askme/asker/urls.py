from django.urls import path
from .views import *

urlpatterns = [
    path('', newQuestions, name="NewQuestions"),
    path('questions/', questions, name="Questions"),
    path('questions/hot/', hotQuestions, name='HotQuestions'),
    path('questions/<int:pk>/', questionDetail, name='QuestionDetail'),
    path('tags/', tags, name='Tags'),
    path('tags/<str:slug>/', tagDetail, name="TagDetail"),
    path('ask/', ask, name="ask"),
    path('settings/', settings, name="settings"),
    path('login/', login, name="login"),
    path('signout/', signout, name='signout'),
    path('registration/', registration, name="Registration"),
    path('users/', users, name="Users"),
    path('users/best/', topUsers, name="topUsers"),
    path('users/<int:pk>/', userDetail, name="userDetail"),

    # path('login_sem/', login, name="login"),
]