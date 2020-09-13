from rest_framework import permissions, viewsets
from rest_framework.throttling import UserRateThrottle

from apps.wordapp.models import Translate, Word

from .serializers import TranslateSerializer, WordSerializer


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
