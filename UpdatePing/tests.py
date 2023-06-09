from django.test import TestCase
from .models import Game
# Create your tests here.

class GameModelTests(TestCase):
    def test_getAppIdFromGameTitle(self):
        'test_getAppIdFromGameTitle returns 393380 when given title "Squad"'
        actualValue = Game.get_app_Id_from_game_title("Squad")
        expectedValue = 393380
        self.assertEquals(actualValue, expectedValue)
    
    def test_get_game_from_steam(TestCase):
        'test get_game_from_steam returns "Squad"'