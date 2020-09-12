from django.contrib.auth import get_user_model
from django.test import TestCase

UserModel = get_user_model()


class LoginTest(TestCase):
    credentials = {"username": "testuser", "password": "test.password"}

    def setUp(self):
        UserModel.objects.create_user(**credentials)

    def test_login(self):
        response = self.client.login(**credentials)
        self.assertTrue(response)

    def test_not_login(self):
        response = self.client.login(
            username=self.username, password="wrong.password"
        )
        self.assertFalse(response)
