from django.db.models import Q

from callback.services import BaseService


class PlayerService(BaseService):
    def check_player_data(self, name: str, email: str) -> bool:
        """
        Проверяет, существует ли пользователь с заданным именем или электронной почтой.
        Возвращает True, если пользователь уникален, и False в противном случае.
        """
        return self.model.objects.filter(Q(name=name) | Q(email=email)).exists()
