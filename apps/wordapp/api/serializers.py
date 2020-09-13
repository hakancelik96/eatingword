from rest_framework import serializers

from apps.wordapp.models import Translate, Word


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ["id", "word", "language", "created_at", "updated_at"]


class TranslateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translate
        fields = ["id", "source", "target", "created_at", "updated_at"]
