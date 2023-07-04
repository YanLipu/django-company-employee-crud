from django.conf import settings
from rest_framework import authentication, exceptions
import jwt

from django.contrib.auth.models import User


class CustomUserAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        print('authenticate')
        token = request.COOKIES.get('jwt')
        print(token)

        if not token:
            return None

        try:
            payload = jwt.decode(token, settings.SECRET_JWT, algorithms=["HS256"])
        except:
            raise exceptions.AuthenticationFailed("Unauthorized")

        user = User.objects.filter(username=payload["username"]).first()
        print(user)

        return (user, None)

class GetTokenParameters:
    def token_payload(self, request):
        token = request.COOKIES.get('jwt')
        print(token)

        if not token:
            return None
        try:
            payload = jwt.decode(token, settings.SECRET_JWT, algorithms=["HS256"])
        except:
            raise exceptions.AuthenticationFailed("Unauthorized")

        return payload