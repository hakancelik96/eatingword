from django.contrib import admin
from django.urls import include, path
from django.views import generic
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path("", include("apps.wordapp.urls")),
    path("admin/", admin.site.urls),
    path("account/", include("apps.account.urls")),
    # API
    path(
        "api/v1/account/",
        include("apps.account.api.urls"),
    ),
    path(
        "api/v1/word/",
        include("apps.wordapp.api.urls"),
    ),
    # openapi-schema
    path(
        "api/v1/openapi/",
        get_schema_view(
            title="Eating Word API",
            description="API for all things …",
            version="1.0.0",
        ),
        name="openapi-schema",
    ),
    # api docs
    path(
        "api/v1/docs/",
        generic.TemplateView.as_view(
            template_name="redoc.html",
            extra_context={"schema_url": "openapi-schema"},
        ),
        name="redoc",
    ),
]
