from django.test import TestCase
from .models import Game
# Create your tests here.

class GameModelTests(TestCase):
    def test_getAppIdFromGameTitle(self):
        'test_getAppIdFromGameTitle returns 393380 when given title "Squad"'
        actualValue = Game.get_app_Id_from_game_title("Squad")
        expectedValue = 393380
        self.assertEquals(actualValue, expectedValue)
    
    def test_get_newsfeed_from_steam(self):
        'test get_newsfeed_from_steam returns a non empty json given app id for Squad'
        actualValue = Game.get_newsfeed_from_steam(393380)
        self.assertTrue(actualValue['appnews'])

    def test_get_game_name(self):
        "test get_game_name returns title 'Squad' given its app id"
        actualValue = Game.get_game_name(393380)
        expectedValue = 'Squad'
        self.assertEquals(actualValue, expectedValue)