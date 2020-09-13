from django.contrib.auth import get_user_model
from rest_framework import serializers

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    known_words = serializers.StringRelatedField(many=True)
    unknown_words = serializers.StringRelatedField(many=True)

    class Meta:
        model = UserModel
        fields = [
            "username",
            "known_words",
            "unknown_words",
            "date_joined",
        ]
        read_only_fields = ["known_words", "unknown_words"]
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {"write_only": True},
        }
