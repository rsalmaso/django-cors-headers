from django.apps import AppConfig
from django.core import checks

from .checks import check_settings


class CorsHeadersConfig(AppConfig):
    name = "corsheaders"

    def ready(self):
        checks.register(check_settings)
