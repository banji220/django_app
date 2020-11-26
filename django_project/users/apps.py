from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def reay(self):
        import users.signals