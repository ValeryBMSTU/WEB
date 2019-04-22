from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import *
from .utils import ObjectsDetailMixing

# def index(request):
#     questions = Question.objects.all()
#     return render(request, 'asker/index.html', context = {'questions': questions})

# def questions(request):
#     questions = Question.objects.all()
#     return render(request, 'asker/questions.html', context = {'questions': questions})

# def questionDetail(request, slug):
#     question = Question.objects.get(slug__iexact=slug)
#     return render(request, 'asker/questionDetail.html', context={'question': question})

# def tags(request):
#     tags = Tag.objects.all()
#     return render(request, 'asker/tags.html', context={'tags': tags})

# def tagDetail(request, pk):
#     tag = Tag.objects.get(pk=pk)
#     return render(request, 'asker/tagDetail.html', context={'tag': tag})

# def ask(request):
#     return render(
#         request,
#         'asker/ask.html',
#         {"values": ['Какая-то дичь', '8-916-416-86-67']}
#     )

# def settings(request):
#     return render(
#         request,
#         'asker/settings.html',
#         {"asker": []}
#     )
# def login(request):
#     return render(
#         request,
#         'asker/login.html',
#         {"asker": []}
#     )
# def registration(request):
#     return render(
#         request,
#         'asker/registration.html',
#         {"asker": []}
#     )
# def users(request):
#     return render(
#         request,
#         'asker/users.html',
#         {"asker": []}
#     )

class Users(View):

    def get(self, request):
        return render(request, 'asker/users.html', context={})

class Registration(View):

    def get(self, request):
        return render(request, 'asker/registration.html', context={})

class Login(View):

    def get(self, request):
        return render(request, 'asker/login.html', context={})

class Settings(View):

    def get(self, request):
        return render(request, 'asker/settings.html', context={})

class Ask(View):

    def get(self, request):
        return render(request, 'asker/ask.html', context={})

class Questions(View):

    def get(self, request):
        questions = Question.objects.all()
        return render(request, 'asker/questions.html', context={'questions': questions})

class NewQuestions(View):

    def get(self, request):
        questions = Question.objects.order_by("-createDate")
        return render(request, 'asker/questions.html', context={'questions': questions})

class HotQuestions(View):

    def get(self, request):
        questions = Question.objects.all()
        return render(request, 'asker/questions.html', context={'questions': questions})

class QuestionDetail(View):
    # model = Question
    # template = 'asker/questionDetail.html'
    def get(self, request, pk):
        # question = Question.objects.get(pk=pk)
        question = get_object_or_404(Question, pk=pk)
        return render(request, 'asker/questionDetail.html', context={'question': question})

class Tags(View):

    def get(self, request):
        tags = Tag.objects.all()
        return render(request, 'asker/tags.html', context={'tags': tags})


class TagDetail(View):
    # model = Tag
    # template = 'asker/tagDetail.html'
    def get(self, request, slug):
        # tag = Tag.objects.get(pk=pk)
        tag = get_object_or_404(Tag, slug=slug)
        return render(request, 'asker/tagDetail.html', context={'tag': tag})

