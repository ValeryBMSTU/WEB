from django.db import models

class Category(models.Model):
    Type = models.CharField(max_length = 32, unique = True)

    def __str__(self):
        return self.Type
    def get_absolute_url(self):
        return '/catego/%d/' % self.pk

class Status(models.Model):
    views = models.IntegerField(default = 0)
    LikeDislikeBalance = models.IntegerField(default = 0)

    def __str__(self):
        return self.pk

class Tag(models.Model):
    TagName = models.CharField(max_length = 16, unique = True)
    def __str__(self):
        return self.TagName

class Question(models.Model):
    Title = models.CharField(max_length = 128)
    Text = models.TextField()
    Autor = models.CharField(max_length = 32)
    CreateDate = models.DateTimeField()
    category = models.ForeignKey(Category, null = True, on_delete = models.PROTECT)
    status = models.OneToOneField(Status, on_delete = models.PROTECT)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.Title
    def get_absolute_url(self):
        return '/post/5d/' % self.pk
    class Meta:
        db_table = 'Questions'

class Answer(models.Model):
    Text = models.TextField()
    Autor = models.CharField(max_length = 32)
    LikeDislikeBalance = models.IntegerField(default = 0)
    question = models.ForeignKey(Question, null = True, on_delete = models.PROTECT)

    def __str__(self):
        return self.Title

class User(models.Model):
    Login = models.CharField(max_length = 32)
    Email = models.EmailField()
    NickName = models.CharField(max_length = 32)
    Password = models.CharField(max_length = 32)
    AvatarURL = models.CharField(max_length = 64)
    Karma = models.IntegerField(default = 0)

    def __str__(self):
        return self.Login
    def get_absolute_url(self):
        return '/users/%d/' % self.pk
    

