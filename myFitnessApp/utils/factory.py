import factory
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class UserFactory(factory.Factory):
    class Meta:
        model = UserModel

    email = 'ivo@app.com'


class AdminFactory(factory.Factory):
    class Meta:
        model = UserModel

    email = 'ivo@app.com'
    is_staff = True
    is_superuser = True