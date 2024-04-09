from django.db import transaction


class BaseService:
    def __init__(self, model):
        self.model = model

    def create_instance(self, **kwargs):
        """
        Create new object with transaction.
        """
        with transaction.atomic():
            instance = self.model(**kwargs)
            instance.save()
            return instance

    def check_instance_exists(self, **kwargs) -> bool:
        """
        Check if object exists using kwargs.
        """
        return self.model.objects.filter(**kwargs).exists()
