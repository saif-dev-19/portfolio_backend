from django.apps import AppConfig
import time
from django.db import connections


class PortfolioConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "portfolio"


def wait_for_db():
    for i in range(10):
        try:
            connections["default"].cursor()
            return
        except Exception:
            time.sleep(2)