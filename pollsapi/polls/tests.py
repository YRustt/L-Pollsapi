from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase, APIClient

from . import apiviews
from . import models


class PollTest(APITestCase):
    def setUp(self):
        self.user = self.setup_user()

        self.client = APIClient()
        self.client.login(username="test", password="test")
        self.uri = '/polls/'

    def setup_user(self):
        User = get_user_model()
        return User.objects.create_user(
            "test",
            password="test"
        )

    def test_list(self):
        response = self.client.get(self.uri)

        self.assertEqual(
            response.status_code, 200,
            f"Expected Response Code 200, received {response.status_code} instead"
        )

    def test_create(self):
        params = {
            "question": "Am I God?",
            "created_by": 1,
        }
        response = self.client.post(self.uri, params)

        self.assertEqual(
            response.status_code, 201,
            f"Expected Response Code 201, received {response.status_code} instead"
        )
