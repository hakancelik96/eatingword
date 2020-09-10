from django.conf import settings
from django.test import TestCase
from django.urls import reverse

REGISTER_URL = reverse("account:register")
FORM_DATA = {
    "username": "testuser",
    "password1": "Test.password",
}


class RegisterTest(TestCase):
    def test_register(self):
        FORM_DATA["password2"] = "Test.password"
        response = self.client.post(REGISTER_URL, FORM_DATA)
        self.assertRedirects(response, reverse(settings.LOGIN_REDIRECT_URL))

    def test_register_form_invalid(self):
        FORM_DATA["password2"] = "Wrong.password"
        response = self.client.post(REGISTER_URL, FORM_DATA)
        self.assertFormError(
            response,
            "form",
            "password2",
            "The two password fields didn’t match.",
        )
