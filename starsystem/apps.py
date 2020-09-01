from django.apps import AppConfig


class StarsystemConfig(AppConfig):
    name = 'starsystem'

    def ready(self):
        import starsystem.signals
