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
        url = f"https://store.steampowered.com/api/storesearch/?term={app_name}&l=english&cc=us"
    
        try:
            response = requests.get(url)
            data = response.json()
            if data['total'] > 0:
                app_id = data['items'][0]['id']
                return int(app_id)
        except requests.exceptions.RequestException as e:
            print("Error occurred while making the API call:", e)
    
        return None

    @staticmethod
    def get_newsfeed_from_steam(app_id):
        url=f"https://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?appid={app_id}&count=3&maxlength=300"

        try:
            response = requests.get(url)
            data = response.json()
            return data
        except Exception as e:
            print("Error occurred while making the API call:", e)
    
        return None

    @staticmethod
    def get_game_name(app_id):
        url = f"http://api.steampowered.com/ISteamApps/GetAppList/v2"
        try:
            response = requests.get(url)
            data = response.json()
            for app in data["applist"]["apps"]:
                if app["appid"] == app_id:
                    return app["name"]
        except Exception as e:
            print(e)
        return None
    
# Create your models here.
class User(models.Model):
    phoneNumber = models.CharField(max_length=200)
    games = models.ManyToManyField('UpdatePing.Game', related_name="user_games")
    def __str__(self):
        return self.phoneNumber