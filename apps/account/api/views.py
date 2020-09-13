from django.contrib.auth import get_user_model
from rest_framework import permissions, viewsets
from rest_framework.throttling import UserRateThrottle

from .serializers import UserSerializer

UserModel = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""

    queryset = UserModel.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)
    throttle_classes = (UserRateThrottle,)
