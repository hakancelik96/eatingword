from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from apps.forms import SemanticFormMixin

UserModel = get_user_model()


class RegisterForm(SemanticFormMixin, UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
