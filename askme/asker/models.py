import requests
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class QuestionManager(models.Manager):
    def best_question(self):
        return self.filter(LikeDislikeBalance__gt=100)
    def new_question(self):
        return self.order_by(CreateDate)

class Category(models.Model):
    categoryType = models.CharField(max_length = 32, unique = True)

    def __str__(self):
        return self.categoryType
    def get_absolute_url(self):
        return '/catego/%d/' % self.pk

class Status(models.Model):
    views = models.IntegerField(default = 0)
    likeDislikeBalance = models.IntegerField(default = 0)

class Tag(models.Model):
    tagName = models.CharField(max_length = 16, unique = True)
    def __str__(self):
        return self.tagName

class Question(models.Model):
    title = models.CharField(max_length = 128)
    text = models.TextField()
    createDate = models.DateTimeField()
    status = models.OneToOneField(Status, on_delete = models.PROTECT)
    user = models.ForeignKey(User, on_delete = models.PROTECT)
    category = models.ForeignKey(Category, null = True, on_delete = models.PROTECT)
    tags = models.ManyToManyField(Tag)
    #objects = QuestionManager()
    #objects =  models.Manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('question_detail', args=[self.pk])

class Answer(models.Model):
    text = models.TextField()
    likeDislikeBalance = models.IntegerField(default = 0)
    question = models.ForeignKey(Question, null = True, on_delete = models.PROTECT)
    user = models.ForeignKey(User, on_delete = models.PROTECT)

    def __str__(self):
        return self.title

class Profile(models.Model):
    nickName = models.CharField(max_length = 32)
    avatarURL = models.CharField(max_length = 64)
    karma = models.IntegerField(default = 0)
    user = models.OneToOneField(User, on_delete = models.PROTECT)

    def __str__(self):
        return self.login
    def get_absolute_url(self):
        return '/users/%d/' % self.pk
    

