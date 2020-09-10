from django.contrib.auth import get_user_model
from rest_framework import permissions, viewsets
from rest_framework.throttling import UserRateThrottle

from apps.restapi.serializers import (
    TranslateSerializer,
    UserSerializer,
    WordSerializer,
)
from apps.wordapp.models import Translate, Word

UserModel = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""

    queryset = UserModel.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)
    throttle_classes = (UserRateThrottle,)


class WordViewSet(viewsets.ModelViewSet):
    """API endpoint that allows words to be viewed or edited."""

    queryset = Word.objects.all()
    serializer_class = WordSerializer
    permission_classes = (permissions.IsAuthenticated,)
    throttle_classes = (UserRateThrottle,)


class TranslateViewSet(viewsets.ModelViewSet):
    """API endpoint that allows translate to be viewed or edited."""

    queryset = Translate.objects.all()
    serializer_class = TranslateSerializer
    permission_classes = (permissions.IsAuthenticated,)
    throttle_classes = (UserRateThrottle,)
