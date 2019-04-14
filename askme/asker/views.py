from django.shortcuts import render
# Create your views here.

def index(request):
    return render(
        request,
        'asker/index.html',
        {"asker": []}
    )
def tag(request):
    return render(
        request,
        'asker/tag.html',
        {"asker": []}
    )
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