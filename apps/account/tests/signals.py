from django.contrib.auth import get_user_model
from django.test import TestCase

from apps.wordapp.models import Translate, Word

UserModel = get_user_model()


class SignalTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        source = Word.objects.create(word="source", language="en")
        target = Word.objects.create(word="kaynak", language="tr")
        cls.translate = Translate.objects.create(source=source, target=target)
        credentials = {"username": "testuser", "password": "test.password"}
        cls.user = UserModel.objects.create_user(**credentials)

    def test_add_known_word(self):
        self.user.known_words.add(self.translate)
        self.assertEqual(self.user.known_words.first(), self.translate)
        self.assertFalse(self.user.unknown_words.all())

    def test_add_unknown_word(self):
        self.user.unknown_words.add(self.translate)
        self.assertEqual(self.user.unknown_words.first(), self.translate)
        self.assertFalse(self.user.known_words.all())

    def test_add_all_before_known(self):
        self.user.known_words.add(self.translate)
        self.user.unknown_words.add(self.translate)
        self.assertEqual(self.user.unknown_words.first(), self.translate)
        self.assertFalse(self.user.known_words.all())

    def test_add_all_before_unknown(self):
        self.user.unknown_words.add(self.translate)
        self.user.known_words.add(self.translate)
        self.assertEqual(self.user.known_words.first(), self.translate)
        self.assertFalse(self.user.unknown_words.all())
