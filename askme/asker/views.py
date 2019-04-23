from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import *
from django.core.paginator import Paginator
from .utils import *

class Users(TagsAndUsersMixing, View):
    template = 'asker/users.html' 

class Registration(TagsAndUsersMixing, View):
    template = 'asker/registration.html'

class Login(TagsAndUsersMixing, View):
    template = 'asker/login.html'

class Settings(TagsAndUsersMixing, View):
    template = 'asker/settings.html'

class Ask(TagsAndUsersMixing, View):
    template = 'asker/ask.html'

class Questions(PaginatorMixing, View):
    model = Question
    header = 'Questions:'
    template = 'asker/questions.html'

class NewQuestions(PaginatorMixing, View):
    model = Question
    header = 'New Questions:'
    template = 'asker/questions.html'

class HotQuestions(PaginatorMixing, View):
    model = Question
    header = 'Hot Questions:'
    template = 'asker/questions.html'

class Tags(TagsAndUsersMixing, View):
    template = 'asker/tags.html'

class QuestionDetail(View):

    def get(self, request, pk):
        question = get_object_or_404(Question, pk=pk)
        answers = question.answers.all()
        tags = Tag.objects.all()
        users = User.objects.all()

        return render(request, 'asker/questionDetail.html', context={'question': question, 'answers': answers, 'tags': tags, 'users': users})


class TagDetail(View):
    def get(self, request, slug):
        tag = get_object_or_404(Tag, slug=slug)
        questionsList = tag.questions.all()
        tags = Tag.objects.all()
        users = User.objects.all()

        paginator = Paginator(questionsList, 2)
        page = request.GET.get('page')
        questions = paginator.get_page(page)

        return render(request, 'asker/tagDetail.html', context={'questions': questions, 'tag': tag, 'tags': tags, 'users': users})

