from django.urls import include, path
from django.views import generic
from rest_framework import routers
from rest_framework.schemas import get_schema_view

from apps.restapi import views

app_name = "restapi"

router = routers.DefaultRouter()
router.register("users", views.UserViewSet)
router.register("word", views.WordViewSet)
router.register("translate", views.TranslateViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
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
        "docs/",
        generic.TemplateView.as_view(
            template_name="redoc.html",
            extra_context={"schema_url": "restapi:openapi-schema"},
        ),
        name="redoc",
    ),
]
