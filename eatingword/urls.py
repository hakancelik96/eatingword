from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("apps.wordapp.urls", namespace="wordapp")),
    path("admin/", admin.site.urls),
    path("account/", include("apps.account.urls", namespace="account")),
    path("restapi/", include("apps.restapi.urls", namespace="restapi")),
]
