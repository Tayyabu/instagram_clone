from django.apps import AppConfig


class ApiConfig(AppConfig):
    name = "api"

    def ready(self) -> None:
        from api.signals import set_posts_permissions
