from django.contrib import admin

from apps.wordapp.models import Translate, Word


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_filter = ["language"]
    search_fields = ["language"]


admin.site.register(Translate)
