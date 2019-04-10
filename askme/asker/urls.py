from django.conf.urls import url
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('tag', views.tag, name="tag"),
    path('ask/', views.ask, name="ask"),
    path('question/', views.question, name="question"),
    path('settings/', views.settings, name="settings"),
    path('login/', views.login, name="login"),
    path('registration/', views.registration, name="registration")
]
