from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "synchro_shop.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import synchro_shop.users.signals  # noqa F401
        except ImportError:
            pass
