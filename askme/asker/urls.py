from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index, name="index"),
    path('questions/', questions, name='questions'),
    path('questions/<int:pk>/', QuestionDetail.as_view(), name='questionDetail'),
    path('tags/', tags, name='tags'),
    path('tags/<int:pk>/', TagDetail.as_view(), name="tagDetail"),

    path('ask/', ask, name="ask"),
    path('question/', question, name="question"),
    path('settings/', settings, name="settings"),
    path('login/', login, name="login"),
    path('registration/', registration, name="registration"),
    path('users/', users, name="users"),
    # path('questionsByDate/', QuestionByDateView.as_view(), name='questionsByDate'),
    # path('questionsByRate/', QuestionByRateView.as_view(), name='questionsByRate'),
    # path('questionsByTag/', QuesStionByTagView.as_view(), name='questionsByTag'),
    # path('questions/<int:number>/', questions_detail, name='question_detail'),
    # path('questions/', ListView.as_view(queryset=Question.objects.all().order_by("title")[:10], template_name="asker/questions.html")),
]