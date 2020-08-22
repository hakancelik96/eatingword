from django import forms

from apps.forms import SemanticFormMixin
from apps.wordapp.models import LANG_CHOICES


class UserTranslateForm(SemanticFormMixin, forms.Form):
    source = forms.CharField(widget=forms.TextInput(attrs={"readonly": ""}))
    source_language = forms.ChoiceField(choices=LANG_CHOICES)
    target = forms.CharField(widget=forms.TextInput())
    target_language = forms.ChoiceField(choices=LANG_CHOICES)
