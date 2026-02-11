from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken


class CustomUser:
    """Utilisateur personnalisé sans dépendance à la base de données"""

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.is_authenticated = True
        self.is_active = True
        self.is_anonymous = False


class JWTAuthenticationWithoutDB(JWTAuthentication):
    """
    Authentification JWT qui extrait les infos utilisateur du token
    sans requête à la base de données
    """

    def get_user(self, validated_token):
        """
        Récupère l'utilisateur depuis le token JWT
        au lieu de la base de données
        """
        try:
            user_id = validated_token.get('user_id')
            username = validated_token.get('username')

            if user_id is None:
                raise InvalidToken('Token ne contient pas user_id')

            if username is None:
                # Fallback si username n'est pas dans le token
                username = f'user_{user_id}'

            return CustomUser(user_id=user_id, username=username)

        except KeyError as e:
            raise InvalidToken(f'Token invalide: {str(e)}')