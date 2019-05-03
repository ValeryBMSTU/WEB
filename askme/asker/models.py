import requests
from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation

# Managers

class QuestionManager(models.Manager):
	
	def sortByDate(self):
		return self.all().order_by('createDate').reverse()

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

class LikeDislikeManager(models.Manager):
    use_for_related_fields = True

    def likes(self):
        return self.get_queryset().filter(vote__gt=0)

    def dislikes(self):
        return self.get_queryset().filter(vote__lt=0)

    def sumRating(self):
        return self.get_queryset().filter(vote__gt=0).count() - self.get_queryset().filter(vote__lt=0).count()

# Models


class Tag(models.Model):
    tagName = models.CharField(max_length = 16, unique = True)
    slug = models.SlugField(max_length=128)

    objects = TagManager()

    def __str__(self):
        return self.tagName

    def get_absolute_url(self):
        return reverse('TagDetail', kwargs={'slug': self.slug})

class LikeDislike(models.Model):

    LIKE = 1
    DISLIKE = -1

    VOTE_TYPES = ((LIKE, 'Like'), (DISLIKE, 'Dislike'))

    user = models.ForeignKey(User, null=True, verbose_name='Like author', on_delete=models.CASCADE)
    vote = models.SmallIntegerField(verbose_name='is like', default=VOTE_TYPES[0], choices=VOTE_TYPES)

    content_type = models.ForeignKey(ContentType, default=None, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField(default=-1)
    content_object = GenericForeignKey()

    objects = LikeDislikeManager()

    def __str__(self):
        return "Like from " + self.user.username

class Question(models.Model):
    title = models.CharField(max_length = 128, db_index=True)
    text = models.TextField()
    createDate = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete = models.CASCADE)
    tags = models.ManyToManyField('Tag', blank=True, related_name='questions')

    votes = GenericRelation(LikeDislike, related_query_name='questions')

    objects = QuestionManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('QuestionDetail', kwargs={'pk': self.pk})

class Answer(models.Model):
    text = models.TextField()
    question = models.ForeignKey(Question, null = True, on_delete = models.CASCADE, related_name='answers')
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='answers')

    votes = GenericRelation(LikeDislike, related_query_name='answers')

    objects = AnswerManager()

    def __str__(self):
        return self.text

class Profile(models.Model):
    avatarURL = models.ImageField(null = True)
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    objects = ProfileManager()

    def __str__(self):
        return self.login

    def get_absolute_url(self):
        return '/users/%d/' % self.pk

