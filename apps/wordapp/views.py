import random

from django.contrib import messages
from django.views import generic

from apps.wordapp.forms import UserTranslateForm
from apps.wordapp.models import Translate


class IndexView(generic.FormView):
    template_name = "base.html"
    form_class = UserTranslateForm

    def form_valid(self, form):
        p = {
            "source__word": form.cleaned_data["source"],
            "source__language": form.cleaned_data["source_language"],
            "target__word": form.cleaned_data["target"],
            "target__language": form.cleaned_data["target_language"],
        }
        translate_queryset = Translate.objects.filter(**p)
        if translate_queryset.exists():
            self.request.user.known_words.add(translate_queryset[0])
            messages.success(
                self.request, "Congratulations you got the word right."
            )
        else:
            translate_queryset = Translate.objects.filter(
                source__word=form.cleaned_data["source"],
                source__language=form.cleaned_data["source_language"],
            )
            self.request.user.unknown_words.add(translate_queryset[0])
            messages.warning(self.request, "Sorry you got the word wrong.")
        return super().form_valid(form)

    def get_initial(self):
        translate_queryset = Translate.objects.filter(source__language="en")
        unknown_translate = translate_queryset.difference(
            self.request.user.known_words.all()
        )
        try:
            index = random.randrange(unknown_translate.count())
        except ValueError:
            return {
                "source": "$ End of the words $",
                "source_language": "en",
                "target_language": "tr",
            }
        else:
            return {
                "source": unknown_translate[index].source.word,
                "source_language": "en",
                "target_language": "tr",
            }

    def get_success_url(self):
        return self.request.META["HTTP_REFERER"]
