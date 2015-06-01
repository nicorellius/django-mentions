# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from .registry import Provider


class UserProvider(Provider):
    model = get_user_model()
    # model = User

    def get_title(self, obj):
        return obj.username

    def search(self, request, term):
        return self.get_queryset().filter(username__istartswith=term)
