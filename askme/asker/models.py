import requests
from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User

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
    slug = models.SlugField(max_length=128)
    def __str__(self):
        return self.tagName

    def get_absolute_url(self):
        return reverse('TagDetail', kwargs={'slug': self.slug})

class Question(models.Model):
    title = models.CharField(max_length = 128, db_index=True)
    text = models.TextField()
    slug = models.SlugField(max_length=128, unique=True)
    createDate = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete = models.PROTECT)
    category = models.ForeignKey(Category, null = True, on_delete = models.PROTECT)
    tags = models.ManyToManyField('Tag', blank=True, related_name='questions')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('QuestionDetail', kwargs={'pk': self.pk})

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

class QuestionLikeDisLike(models.Model):
    likeDisLike = models.IntegerField()
    question = models.ForeignKey(Question, on_delete = models.CASCADE, related_name="likes", null=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='likes')

    class Meta:
        unique_together = ('question', 'user',)

class AnswerLikeDisLike(models.Model):
    likeDisLike = models.IntegerField()
    answer = models.ForeignKey(Answer, on_delete = models.CASCADE, related_name="disLikes", null=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='disLikes')

    class Meta:
        unique_together = ('answer', 'user',)
