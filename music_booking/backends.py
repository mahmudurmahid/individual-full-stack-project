from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomAuthBackend(BaseBackend):
    """
    Custom authentication backend to log in users using email and password.
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Find user by email
            user = User.objects.get(email=username)
            if user.check_password(password):  # Check password validity
                return user
        except User.DoesNotExist:
            return None
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
