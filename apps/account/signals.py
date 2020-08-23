from django.contrib.auth import get_user_model
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

UserModel = get_user_model()

__all__ = ["known_words", "unknown_words"]


@receiver(m2m_changed, sender=UserModel.known_words.through)
def signal_known_words(
    sender, instance, action, reverse, model, pk_set, **kwargs
):
    if action == "post_add":
        instance.unknown_words.remove(*pk_set)


@receiver(m2m_changed, sender=UserModel.unknown_words.through)
def signal_unknown_words(
    sender, instance, action, reverse, model, pk_set, **kwargs
):
    if action == "post_add":
        instance.known_words.remove(*pk_set)
