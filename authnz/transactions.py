from django.contrib.auth.models import User
from django.db import transaction


@transaction.atomic
def register_user(username: str, password: str) -> User:
    """
    Register user
    :param username:
    :param password:
    :return:
    """
    user = User(username=username)
    user.set_password(password)
    user.save()
    return user
