from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.wordapp.models import Translate, Word

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    known_words = serializers.StringRelatedField(many=True)
    unknown_words = serializers.StringRelatedField(many=True)

    class Meta:
        model = UserModel
        fields = [
            "username",
            "email",
            "known_words",
            "unknown_words",
            "date_joined",
        ]
        read_only_fields = fields


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ["id", "word", "language", "created_at", "updated_at"]


class TranslateSerializer(serializers.ModelSerializer):
    source = serializers.SlugRelatedField(read_only=True, slug_field="word")
    target = serializers.SlugRelatedField(read_only=True, slug_field="word")

    class Meta:
        model = Translate
        fields = ["id", "source", "target", "created_at", "updated_at"]
