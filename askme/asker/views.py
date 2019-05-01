from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from .models import *
from django.core.paginator import Paginator
from .utils import *
from asker.forms import LoginForm
from django import forms
from django.contrib import auth

def baseRender(request, template='/', obj = None):

    tags = Tag.objects.all()
    users = User.objects.all()	

    return render(request, template, context={'obj': obj, 'tags': tags, 'users': users, 'obj': obj})

def paginatorRender(request, object_list, template='/', header = None, obj = None):

    tags = Tag.objects.all()
    users = User.objects.all()

    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    object_list = paginator.get_page(page)
    # try:
    #     objects_page = p.get_page(page)

    # except PageNotAnInteger:
    #     objects_page = p.get_page(1)

#         paginator = Paginator(questionsList, 2)
#         page = request.GET.get('page')
#         questions = paginator.get_page(page)	


    return render(request, template, {'object_list':  object_list, 'tags': tags, 'users': users, 'obj': obj, 'header': header})


def users(request):
    template = 'asker/users.html'
    return paginatorRender(request, User.objects.all(), template)

def registration(request):
    template =  'asker/registration.html'
    return baseRender(request, template)

def login(request):
    template = 'asker/login.html'
    return baseRender(request, template)

def settings(request):
    template = 'asker/settings.html'
    return baseRender(request, template)

def ask(request):
    template = 'asker/ask.html'
    return baseRender(request, template)

def questions(request):
    template = 'asker/questions.html'
    header = 'Questions:'
    return paginatorRender(request, Question.objects.sortById(), template, header)

def newQuestions(request):
    template = 'asker/questions.html'
    header = 'New Questions:'
    return paginatorRender(request, Question.objects.sortByDate(), template, header)

def hotQuestions(request):
    template = 'asker/questions.html'
    header = 'Hot Questions:'
    return paginatorRender(request, Question.objects.sortByRate(), template, header)

def tags(request):
    template = 'asker/tags.html'
    return paginatorRender(request, Tag.objects.all(), template)

def questionDetail(request, pk):
    template = 'asker/questionDetail.html'

    question = get_object_or_404(Question, pk=pk)
    header = question.title

    count = question.votes.likes().count()

    return paginatorRender(request, question.answers.all(), template, header, question)

def tagDetail(request, slug):
    template = 'asker/tagDetail.html'

    tag = get_object_or_404(Tag, slug=slug)
    header = tag.tagName + ':'

    return paginatorRender(request, tag.questions.all(), template, header, tag)

# class Users(TagsAndUsersMixing, View):
#     template = 'asker/users.html' 

# class Registration(TagsAndUsersMixing, View):
#     template = 'asker/registration.html'

# class Login(TagsAndUsersMixing, View):
#     template = 'asker/login.html'

# class Settings(TagsAndUsersMixing, View):
#     template = 'asker/settings.html'

# class Ask(TagsAndUsersMixing, View):
#     template = 'asker/ask.html'

# class Questions(PaginatorMixing, View):
#     model = Question
#     header = 'Questions:'
#     template = 'asker/questions.html'

# class NewQuestions(PaginatorMixing, View):
#     model = Question
#     header = 'New Questions:'
#     template = 'asker/questions.html'

# class HotQuestions(PaginatorMixing, View):
#     model = Question
#     header = 'Hot Questions:'
#     template = 'asker/questions.html'

# class Tags(TagsAndUsersMixing, View):
#     template = 'asker/tags.html'

# class QuestionDetail(View):

#     def get(self, request, pk):
#         question = get_object_or_404(Question, pk=pk)
#         answers = question.answers.all()
#         tags = Tag.objects.all()
#         users = User.objects.all()

#         return render(request, 'asker/questionDetail.html', context={'question': question, 'answers': answers, 'tags': tags, 'users': users})


# class TagDetail(View):
#     def get(self, request, slug):
#         tag = get_object_or_404(Tag, slug=slug)
#         questionsList = tag.questions.all()
#         tags = Tag.objects.all()
#         users = User.objects.all()

#         paginator = Paginator(questionsList, 2)
#         page = request.GET.get('page')
#         questions = paginator.get_page(page)

#         return render(request, 'asker/tagDetail.html', context={'questions': questions, 'tag': tag, 'tags': tags, 'users': users})


# Seminar

# def login(request):
#     if request.POST:
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cdata = form.cleaned_data
#             user = auth.authenticate(**cdata)
#             if user is not None:
#                 auth.login(request, user)
#                 return redirect
#             # form.add_error
#     else:
#         form = LoginForm()
    
#     return render(request, 'asker/login.html', {'form': form})

# def logout(request):
#     return redirect('/')

# def ask(requests):
    
#     form = AskForm(request.POST)
