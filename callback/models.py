from django.db import models

from mysite.constants import GAME_NAME_MAX_LENGTH, PLAYER_FIELD_MAX_LENGTH


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.__class__.__name__} {getattr(self, 'name', '')}"


class Player(BaseModel):
    name = models.CharField(max_length=PLAYER_FIELD_MAX_LENGTH, default="", unique=True)
    email = models.EmailField(max_length=PLAYER_FIELD_MAX_LENGTH, unique=True)


class Game(BaseModel):
    name = models.CharField(max_length=GAME_NAME_MAX_LENGTH, default="")
    players = models.ManyToManyField(Player, blank=True, related_name="player_games", through="PlayerGame")


class PlayerGame(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.player.name} in {self.game.name}"
