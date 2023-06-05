from django.shortcuts import render
from django.http import HttpResponse
from steamspypi import SteamSpy

def index(request):
    return HttpResponse("Hello, world. You're at the UpdatePing index.")

def get_game_from_steam(request, app_id):
    url = 'http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?appid='+app_id+'&count=3&maxlength=300&format=json'
    r = requests.get(url, headers={'Content-Type':      
        'application/json'})
    game = r.json()
    return HttpResponse("Game is " % game) 

def get_app_Id_from_game_title(request, app_name):
    # Create an instance of the SteamSpy class
    steamspy = SteamSpy()

    # Retrieve the AppID for a game or application
    data = steamspy.appdetails(app_name)
    app_id = data["appid"]

    print("AppID:", app_id)
    return HttpResponse("app ID is " % app_id) 