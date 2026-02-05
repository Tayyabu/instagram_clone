from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'
    def ready(self) -> None:
        from .signals import remove_obj_perms_connected_with_user
