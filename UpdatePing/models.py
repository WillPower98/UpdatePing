from django.db import models
from django.contrib.postgres.fields import ArrayField
import steam
import requests

class Game(models.Model):
    title = models.CharField(max_length=200)
    picture = models.ImageField()

    def __str__(self):
        return self.title

    @staticmethod
    def get_app_Id_from_game_title(app_name):

        # Retrieve the AppID for a game or application
        app_id = steam.search(app_name)

        print("AppID:", app_id)
        return app_id

    @staticmethod
    def get_game_from_steam(app_id):
        url = 'http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?appid='+app_id+'&count=3&maxlength=300&format=json'
        r = requests.get(url, headers={'Content-Type':      
            'application/json'})
        game = r.json()
        return game
    
# Create your models here.
class User(models.Model):
    phoneNumber = models.CharField(max_length=200)
    games = models.ManyToManyField('UpdatePing.Game', related_name="user_games")
    def __str__(self):
        return self.phoneNumber