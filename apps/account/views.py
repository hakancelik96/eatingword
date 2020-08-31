from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views import generic

from apps.account.forms import AuthenticationForm, RegisterForm
from apps.views import MessageMixin


class RegisterView(MessageMixin, generic.CreateView):
    template_name = "registration/register.html"
    success_url = reverse_lazy("wordapp:index")
    form_class = RegisterForm
    success_message = "You have successfully registered %(username)s"

    def form_valid(self, form):
        response = super().form_valid(form)
        if user := authenticate(
            self.request,
            username=self.object.username,
            password=self.object.password,
        ):
            login(self.request, user)
        else:
            messages.error(self.request, "Could not login")
        return response


class LoginView(MessageMixin, auth_views.LoginView):
    form_class = AuthenticationForm
    success_message = "You have successfully logged in %(username)s"
