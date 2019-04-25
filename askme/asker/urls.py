from django.urls import path
from .views import *

urlpatterns = [
    path('', NewQuestions.as_view(), name="NewQuestions"),
    path('questions/', Questions.as_view(), name="Questions"),
    path('questions/hot/', HotQuestions.as_view(), name='HotQuestions'),
    path('questions/<int:pk>/', QuestionDetail.as_view(), name='QuestionDetail'),
    path('tags/', Tags.as_view(), name='Tags'),
    path('tags/<str:slug>/', TagDetail.as_view(), name="TagDetail"),
    path('ask/', Ask.as_view(), name="Ask"),
    path('settings/', Settings.as_view(), name="Settings"),
    path('login/', Login.as_view(), name="Login"),
    # path('login_sem/', login, name="login"),
    path('registration/', Registration.as_view(), name="Registration"),
    path('users/', Users.as_view(), name="Users"),
]