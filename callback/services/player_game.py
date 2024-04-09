from callback.services import BaseService


class PlayerGameService(BaseService):
    def check_game_is_full(self, game_id):
        return self.model.objects.filter(game_id=game_id).count() >= 5
