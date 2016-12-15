from __future__ import unicode_literals

from django.apps import AppConfig


class SheldonAuthConfig(AppConfig):
    name = 'auth'
    label = 'sheldon_auth'

    def ready(self):
        from . import signals
