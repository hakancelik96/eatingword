from rest_framework import serializers

from apps.wordapp.models import Translate, Word


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
