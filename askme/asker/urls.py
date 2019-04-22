from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('questions/', Questions.as_view(), name='questions'),
    path('questions/<int:pk>/', QuestionDetail.as_view(), name='questionDetail'),
    path('tags/', Tags.as_view(), name='tags'),
    path('tags/<int:pk>/', TagDetail.as_view(), name="tagDetail"),
    path('ask/', Ask.as_view(), name="ask"),
    path('settings/', Settings.as_view(), name="settings"),
    path('login/', Login.as_view(), name="login"),
    path('registration/', Registration.as_view(), name="registration"),
    path('users/', Users.as_view(), name="users"),
]