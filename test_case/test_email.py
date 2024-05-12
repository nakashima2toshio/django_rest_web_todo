# Test: test_email.py
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model, login


class MyTestCase(TestCase):
    User = get_user_model()

    def setUp(self):
        self.client = Client()

        # create user: http://localhost:8000/api/auth/users/
        self.signup_url = reverse("accounts:account_signup")

        # activate user: http://localhost:8000/api/auth/users/activation/
        self.activation_url = reverse("accounts:account_activation_sent")

        self.login_url = reverse("accounts:account_login")

        self.signup_data = {
            "email": "test@example.com",
            "password1": "testpassword123",
            "password2": "testpassword123",
            "name": "Test User"
        }

    def test_something(self):
        return self.assertEqual(True, True, msg="OK!!")  # add assertion here

    def tearDown(self) -> None:
        pass
