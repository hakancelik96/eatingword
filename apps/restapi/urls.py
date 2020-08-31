from django.urls import include, path
from rest_framework import routers

from apps.restapi import views

app_name = "restapi"

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"word", views.WordViewSet)
router.register(r"translate", views.TranslateViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
]
