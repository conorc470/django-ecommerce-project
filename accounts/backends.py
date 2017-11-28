
from django.contrib.auth.models import User


class EmailAuth(object):
    """
    Authenticate a of User by an exact match on the email and password.
    """

    # Note: Even though this method validates an email address,
    #       the argument to authenticate must be called 'username'
    def authenticate(self, username=None, password=None):
        """
        Get an instance of User using the supplied email
        and verify the password
        """
        try:
            # Get a User instance using the supplied email
            user = User.objects.get(email=username)

            # Check if the password submitted matches that of this User
            if user.check_password(password):
                return user
            return None

        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        """
        Used by the Django authentication system to retrieve a User instance
        """
        try:
            user = User.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None

        except User.DoesNotExist:
            return None