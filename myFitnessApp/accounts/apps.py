from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myFitnessApp.accounts'

    def ready(self):
        import myFitnessApp.accounts.signals