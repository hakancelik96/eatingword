from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path

from apps.account.views import LoginView, RegisterView
from apps.wordapp.views import IndexView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("admin/", admin.site.urls),
]
