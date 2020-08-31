from django.urls import path

from apps.wordapp.views import IndexView

app_name = "wordapp"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]
