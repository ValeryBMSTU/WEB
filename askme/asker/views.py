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
        {"asker": []}
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
