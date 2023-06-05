from django.db import models
from django.contrib.postgres.fields import ArrayField

class Game(models.Model):
    title = models.CharField(max_length=200)
    pictre = models.ImageField()
    def __str__(self):
        return self.title

# Create your models here.
class User(models.Model):
    phoneNumber = models.CharField(max_length=200)
    games = models.ManyToManyField('UpdatePing.Game', related_name="user_games")
    def __str__(self):
        return self.phoneNumber