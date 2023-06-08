from django.http import HttpResponse
from models import Game

def index(request):
    games_list = Game.objects.order_by("title")
    output = games_list
    return HttpResponse(output)

    