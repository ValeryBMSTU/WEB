from django.contrib import admin
from asker.models import Answer, Question, Tag, Profile, Status, Category

admin.site.register(Question)
admin.site.register(Category)
admin.site.register(Status)
admin.site.register(Tag)
admin.site.register(Answer)
admin.site.register(Profile)
