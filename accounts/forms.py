from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class UserAdminCreationForm(UserCreationForm):
    """
    A Custom form for creating new users.
    """

    class Meta:
        model = CustomUser
        fields = '__all__'