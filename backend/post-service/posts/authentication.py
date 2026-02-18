from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken


class CustomUser:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.is_authenticated = True
        self.is_active = True
        self.is_anonymous = False


class JWTAuthenticationWithoutDB(JWTAuthentication):
    def get_user(self, validated_token):
        try:
            user_id = validated_token.get('user_id')
            username = validated_token.get('username')

            if user_id is None:
                raise InvalidToken('Token ne contient pas user_id')

            if username is None:
                username = f'user_{user_id}'

            return CustomUser(user_id=user_id, username=username)

        except KeyError as e:
            raise InvalidToken(f'Token invalide: {str(e)}')