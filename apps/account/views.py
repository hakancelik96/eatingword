from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import generic

from apps.account.forms import RegisterForm
from apps.views import MessageMixin


class RegisterView(MessageMixin, generic.CreateView):
    template_name = "registration/register.html"
    success_url = reverse_lazy("index")
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


class LoginView(MessageMixin, LoginView):
    success_message = "You have successfully logged in %(username)s"
