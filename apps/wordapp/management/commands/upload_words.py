from contextlib import suppress
from pathlib import Path

from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from googletrans import Translator

from apps.wordapp.models import Translate, Word


class Command(BaseCommand):
    help = "Upload words to the database."

    def handle(self, *args, **kwargs):
        english_words = Path(
            "apps/wordapp/management/commands/words/english.txt"
        ).open()
        for word in english_words.readlines():
            with suppress(IntegrityError):
                en_word, en_created = Word.objects.get_or_create(
                    word=self.clean_word(word), language="en"
                )
                if en_created:
                    tr_word, __ = Word.objects.get_or_create(
                        word=Translator()
                        .translate(self.clean_word(word), "tr")
                        .text.lower(),
                        language="tr",
                    )
                    translate, created = Translate.objects.get_or_create(
                        source=en_word, target=tr_word
                    )
                    if created:
                        self.stdout.write(
                            self.style.SUCCESS(
                                f"Successfully created {translate}"
                            )
                        )

    @staticmethod
    def clean_word(word):
        return word.replace("\n", "")
