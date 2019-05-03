from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from .models import *
from django.core.paginator import Paginator
from asker.forms import *
from django import forms
from django.contrib import auth
from django.db.models import Count
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

def baseRender(request, template='/', obj = None):

    tags = Tag.objects.all()
    users = User.objects.all()	

    return render(request, template, context={'obj': obj, 'tags': tags, 'users': users, 'obj': obj})

def paginatorRender(request, object_list, template='/', header = None, obj = None):

    tags = Tag.objects.all()
    users = User.objects.all()

    paginator = Paginator(object_list, 5)
    page = request.GET.get('page')
    object_list = paginator.get_page(page)

    return render(request, template, {'object_list':  object_list, 'obj': obj, 'header': header})


def users(request):
    template = 'asker/users.html'
    return paginatorRender(request, User.objects.all(), template)

def questions(request):
    template = 'asker/questions.html'
    header = 'Questions:'
    return paginatorRender(request, Question.objects.sortById().annotate(numb_answers=Count('answers')), template, header)

def newQuestions(request):
    template = 'asker/questions.html'
    header = 'New Questions:'
    return paginatorRender(request, Question.objects.sortByDate().annotate(numb_answers=Count('answers')), template, header)

def hotQuestions(request):
    template = 'asker/questions.html'
    header = 'Hot Questions:'
    return paginatorRender(request, Question.objects.annotate(numb_answers=Count('answers')).order_by('-numb_answers'), template, header)

def tags(request):
    template = 'asker/tags.html'
    return paginatorRender(request, Tag.objects.all(), template)

def tagDetail(request, slug):
    template = 'asker/tagDetail.html'

    tag = get_object_or_404(Tag, slug=slug)
    header = tag.tagName + ':'

    return paginatorRender(request, tag.questions.all(), template, header, tag)


def fillErrors(formErrors, errors):
    for i in formErrors:
        formattedFieldName = i.replace('_', ' ')
        errors.append(f' { formattedFieldName } field error: {formErrors[i][0]}')


def registration(request):

    tags = Tag.objects.all()
    users = User.objects.all()	

    errors = []
    form = UserSignUpForm
    if request.method == 'POST':
        form = form(request.POST)
        if request.POST['password'] != request.POST['password_confirmation']:
            errors.append('Passwords don\'t match')
        elif form.is_valid():
            user = User.objects.create(username=request.POST['username'],
                                       email=request.POST['email'],
                                       first_name=request.POST['first_name'],
                                       last_name=request.POST['last_name'])
            user.set_password(request.POST['password_confirmation'])
            user.save()
            auth_login(request, user)
            return redirect('/asker/questions')
        else:
            fillErrors(form.errors, errors)
    else:
        auth_logout(request)

    return render(request, 'asker/registration.html', {'form': form, 'messages': errors, 'tags': tags, 'users': users})

def login(request):

    tags = Tag.objects.all()
    users = User.objects.all()	

    errors = []
    form = UserSignInForm
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/asker/questions')
        else:
            errors.append('Invalid username or password')

    auth_logout(request)
    return render(request, 'asker/login.html', {'form': form, 'messages': errors, 'tags': tags, 'users': users})

def signout(request):
    if not request.user.is_authenticated:
        raise Http404
    auth_logout(request)
    return redirect('/asker/questions')

@login_required(login_url='/asker/login')
def settings(request):
    errors = []
    form = UserSettingsForm
    if request.method == 'POST':
        form = form(request.POST)
        if form.is_valid():
            for changedField in form.changed_data:
                setattr(request.user, changedField, request.POST[changedField])
            request.user.save()
            return redirect('/asker/questions')
        else:
            fillErrors(form.errors, errors)
    else:
        for i in form.base_fields:
            form.base_fields[i].widget.attrs['placeholder'] = getattr(request.user, i)
    return render(request, 'asker/settings.html', {'form': form, 'messages': errors})

@login_required(login_url='/asker/login')
def ask(request):
    errors = []
    form = NewQuestionForm
    if request.method == 'POST':
        form = form(request.POST)

        if form.is_valid():
            question = Question.objects.create(user=request.user,
                                               title=request.POST['title'],
                                               text=request.POST['text'])
            question.save()
            for tagTitle in request.POST['tags'].split():
                tag = Tag.objects.get_or_create(tagName=tagTitle, slug=tagTitle)[0]
                question.tags.add(tag)
                question.save()
            return redirect('/asker/questions')
        else:
            fillErrors(form.errors, errors)

    return render(request, 'asker/ask.html', {'form': form, 'messages': errors})

@login_required(login_url='/asker/login')
def questionDetail(request, pk):
    errors = []
    question = get_object_or_404(Question.objects.annotate(numb_answers=Count('answers')), pk=pk)
    object_list = question.answers.all()
    obj = question
    form = WriteAnswerForm
    if request.method == 'POST':
        form = form(request.POST)
        if form.is_valid():
            newAnswer = Answer.objects.create(user=request.user,
                                                text=request.POST['text'],
                                                question=question)
            newAnswer.save()
            return redirect('/asker/questions')
        else:
            fillErrors(form.errors, errors)

    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    object_list = paginator.get_page(page)

    return render(request, 'asker/questionDetail.html', {'obj': obj, 'object_list':  object_list, 'form': form, 'messages': errors})

