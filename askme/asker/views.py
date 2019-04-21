from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, FormMixin
from django.http import HttpResponse
from django.db import transaction
from asker.models import *

def index(request):
    questions = Question.objects.all()
    return render(request, 'asker/index.html', context = {'questions': questions})

def questions(request):
    questions = Question.objects.all()
    return render(request, 'asker/questions.html', context = {'questions': questions})

def questionDetail(request, slug):
    question = Question.objects.get(slug__iexact=slug)
    return render(request, 'asker/questionDetail.html', context={'question': question})

def tags(request):
    tags = Tag.objects.all()
    return render(request, 'asker/tags.html', context={'tags': tags})

def tag(request, pk):
    tag = Tag.objects.get(pk=pk)
    return render(request, 'asker/tag.html', context={'tag': tag})

def ask(request):
    return render(
        request,
        'asker/ask.html',
        {"values": ['Какая-то дичь', '8-916-416-86-67']}
    )
def question(request):
    return render(
        request,
        'asker/question.html',
        {"asker": []}
    )
def settings(request):
    return render(
        request,
        'asker/settings.html',
        {"asker": []}
    )
def login(request):
    return render(
        request,
        'asker/login.html',
        {"asker": []}
    )
def registration(request):
    return render(
        request,
        'asker/registration.html',
        {"asker": []}
    )
def users(request):
    return render(
        request,
        'asker/users.html',
        {"asker": []}
    )

def questions_detail(request, question_id):
    return render(
        request, 
        'questionDetail.html', 
        {'question': get_object_or_404(Question, pk=question_id)}
    )


class QuestionByDateView(ListView):
    template_name = 'asker/questionsBydate.html'

    model = Question
    context_object_name = 'question_list'

    paginate_by = 10

    def get_queryset(self):
        return Question.objects.order_by('-createDate')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_name = self.request.GET.get('tag')
        if tag_name is not None:
            context['tag_query'] = tag_name
            context['question_list'] = Question.objects.filter(tags__text__exact=tag_name)
        context['tag_list'] = Tag.objects.all()
        return context


class QuestionByRateView(ListView):
    template_name = 'asker/questionsByRate.html'

    model = Question
    context_object_name = 'question_list'

    paginate_by = 10

    def get_queryset(self):
        return Question.objects.order_by('-likeDislikeBalance')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_name = self.request.GET.get('tag')
        if tag_name is not None:
            context['tag_query'] = tag_name
            context['question_list'] = Question.objects.filter(tags__text__exact=tag_name)
        context['tag_list'] = Tag.objects.all()
        return context


class QuestionByTagView(ListView):
    template_name = 'asker/questionsByTag.html'
    context_object_name = 'question_list'

    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['tag_list'] = Tag.objects.all()
        return context

    def get_queryset(self):
        return Question.objects.filter(tags__text__exact=self.kwargs['tag_name'])

