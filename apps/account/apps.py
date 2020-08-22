from django.apps import AppConfig


class AccountConfig(AppConfig):
    name = "apps.account"

    # def ready(self):
    #     from apps.account.signals import signal_known_words, signal_unknown_words # unimport: skip
