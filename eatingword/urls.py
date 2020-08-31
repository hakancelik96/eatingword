from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import include, path
from django.views import generic
from rest_framework.schemas import get_schema_view

from apps.account.views import LoginView, RegisterView
from apps.wordapp.views import IndexView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("admin/", admin.site.urls),
    path("api/", include("apps.restapi.urls", namespace="api")),
    path(
        "openapi/",
        get_schema_view(
            title="Eating Word API",
            description="API for all things …",
            version="1.0.0",
        ),
        name="openapi-schema",
    ),
    path(
        "api/docs/",
        generic.TemplateView.as_view(
            template_name="swagger-ui.html",
            extra_context={"schema_url": "openapi-schema"},
        ),
        name="swagger-ui",
    ),
]
