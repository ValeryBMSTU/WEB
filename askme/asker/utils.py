# from django.shortcuts import render, get_object_or_404
# from django.core.paginator import Paginator
# from .models import *

# class PaginatorMixing:
#     model = None
#     header = None
#     template = None


#     def get(self, request, slug = None):
#         if self.header == 'New Questions:':
#             objsList = self.model.objects.order_by("-createDate")
#         else:
#             objsList = self.model.objects.all()
            
#         tags = Tag.objects.all()
#         users = User.objects.all()

#         paginator = Paginator(objsList, 2)
#         page = request.GET.get('page')
#         objs = paginator.get_page(page)

#         return render(request, self.template, context={self.model.__name__.lower() + 's': objs,'tags': tags, 'users': users, 'header': self.header})

# class TagsAndUsersMixing:
#     header = None
#     template = None

#     def get(self, request):
#         tags = Tag.objects.all()
#         users = User.objects.all()
#         return render(request, self.template, context={'tags': tags, 'users': users, 'header': self.header})

# class PaginatorMixing:
#         objsList = None
#         objs = None

#         paginator = Paginator(questionsList, 2)
#         page = request.GET.get('page')
#         questions = paginator.get_page(page)

