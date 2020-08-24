from django.contrib.auth import forms as auth_forms
from django.contrib.auth import get_user_model

from apps.forms import UikitFormMixin

UserModel = get_user_model()


class RegisterForm(UikitFormMixin, auth_forms.UserCreationForm):
    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel


class AuthenticationForm(UikitFormMixin, auth_forms.AuthenticationForm):
    pass
