from callback.models import Game, Player, PlayerGame
from callback.services.game import GameService
from callback.services.player import PlayerService
from callback.services.player_game import PlayerGameService


def player_service():
    return PlayerService(model=Player)


def game_service():
    return GameService(model=Game)


def player_game_service():
    return PlayerGameService(model=PlayerGame)
