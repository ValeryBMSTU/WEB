from django.shortcuts import render, get_object_or_404
from .models import *

class ObjectsDetailMixing:
    model = None
    template = None

    def get(self, request, pk):
        # question = Question.objects.get(pk=pk)
        obj = get_object_or_404(self.model, pk=pk)
        return render(request, self.template, context={self.model.__name__.lower(): obj})
