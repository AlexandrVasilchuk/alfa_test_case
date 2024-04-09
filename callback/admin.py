from django.contrib import admin

from callback.models import Game, Player, PlayerGame


class BaseAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"


@admin.register(Player)
class PlayersAdmin(BaseAdmin):
    list_display = (
        "pk",
        "name",
        "email",
        "created_at",
        "modified_at",
    )
    search_fields = ("name", "email")


class PlayerInline(admin.TabularInline):
    model = PlayerGame
    extra = 1


@admin.register(Game)
class GameAdmin(BaseAdmin):
    list_display = (
        "pk",
        "name",
        "game_players",
        "created_at",
        "modified_at",
    )
    inlines = [
        PlayerInline,
    ]

    @admin.display(description="Players names of this game")
    def game_players(self, game: Game) -> str:
        return ", ".join([player.name for player in game.players.all()])
