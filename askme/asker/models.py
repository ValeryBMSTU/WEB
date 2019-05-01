import requests
from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User

# Managers

class QuestionManager(models.Manager):
	
	def sortByDate(self):
		return self.all().order_by('createDate').reverse()

	def sortByRate(self):
		return self.all().order_by('pk').reverse()

	def sortById(self):
		return self.all().order_by('pk')


class TagManager(models.Manager):
	
	def sortByTag(self, tag_name):
		return self.filter(title=tag_name).first().questions.all().reverse()


class AnswerManager(models.Manager):
	
	def sortByRate(self):
		return self.all().order_by('rating').reverse()


class ProfileManager(models.Manager):
		
	def sortByUsername(self, username):
		return self.all().filter(username=username).first()

# Models

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

    objects = TagManager()

    def __str__(self):
        return self.tagName

    def get_absolute_url(self):
        return reverse('TagDetail', kwargs={'slug': self.slug})

class Question(models.Model):
    title = models.CharField(max_length = 128, db_index=True)
    text = models.TextField()
    slug = models.SlugField(max_length=128, unique=True)
    createDate = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, null = True, on_delete = models.CASCADE)
    tags = models.ManyToManyField('Tag', blank=True, related_name='questions')

    objects = QuestionManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('QuestionDetail', kwargs={'pk': self.pk})

class Answer(models.Model):
    text = models.TextField()
    likeDislikeBalance = models.IntegerField(default = 0)
    question = models.ForeignKey(Question, null = True, on_delete = models.CASCADE, related_name='answers')
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='answers')

    objects = AnswerManager()

    def __str__(self):
        return self.text

class Profile(models.Model):
    nickName = models.CharField(max_length = 32)
    avatarURL = models.CharField(max_length = 64)
    karma = models.IntegerField(default = 0)
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    objects = ProfileManager()

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
