from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

UserModel = get_user_model()


@admin.register(UserModel)
class User(UserAdmin):
    filter_horizontal = UserAdmin.filter_horizontal + (
        "known_words",
        "unknown_words",
    )
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("known_words", "unknown_words")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("known_words", "unknown_words")}),
    )
