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
