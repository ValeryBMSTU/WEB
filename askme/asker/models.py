from django.db import models

class Users(models.Model):
    Login = models.CharField(max_length = 20)
    Emain = models.CharField(max_length = 20)
    NickName = models.CharField(max_length = 20)
    Password = models.CharField(max_length = 32)

    def __str__(self):
        return self.NickName