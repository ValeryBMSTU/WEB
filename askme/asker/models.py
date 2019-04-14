from django.db import models

class Question(models.Model):
    Title = models.CharField(max_length = 64)
    Text = models.TextField()
    Autor = models.CharField(max_length = 20)
    CreateDate = models.DateTimeField()

    def __str__(self):
        return self.Title

class Ask(models.Model):
    Title = models.CharField(max_length = 64)
    Text = models.TextField()
    Autor = models.CharField(max_length = 20)

    def __str__(self):
        return self.Title

class Tag(models.Model):
    TagName = models.CharField(max_length = 20, unique = True)

    def __str__(self):
        return self.TagName
