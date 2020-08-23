from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.models import AbstractTimeModel
from apps.wordapp.models import Translate


class User(AbstractUser, AbstractTimeModel):
    unknown_words = models.ManyToManyField(
        to=Translate, related_name="user_unknown_word", blank=True
    )
    known_words = models.ManyToManyField(
        to=Translate, related_name="user_known_word", blank=True
    )
