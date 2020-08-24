from django import forms

from apps.forms import UikitFormMixin
from apps.wordapp.models import LANG_CHOICES


class UserTranslateForm(UikitFormMixin, forms.Form):
    source = forms.CharField(widget=forms.TextInput(attrs={"readonly": ""}))
    source_language = forms.ChoiceField(
        widget=forms.HiddenInput(), choices=LANG_CHOICES
    )
    target = forms.CharField(widget=forms.TextInput())
    target_language = forms.ChoiceField(
        widget=forms.HiddenInput(), choices=LANG_CHOICES
    )
