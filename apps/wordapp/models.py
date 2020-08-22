from django.db import models

from apps.models import AbstractTimeModel

LANG_CHOICES = (
    ("tr", "Turkish"),
    ("en", "English"),
)


class Word(AbstractTimeModel):
    word = models.CharField(max_length=50)
    language = models.CharField(choices=LANG_CHOICES, max_length=2)

    class Meta:
        unique_together = ["word"]

    def __str__(self):
        return f"{self.language} | {self.word}"


class Translate(AbstractTimeModel):
    source = models.ForeignKey(
        to=Word, related_name="source_word", on_delete=models.CASCADE
    )
    target = models.ForeignKey(
        to=Word, related_name="target_word", on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ["source", "target"]

    def save(self, *args, **kwargs):
        if self.source != self.target:
            super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.source.word} -> {self.target.word}"
