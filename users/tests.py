from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from users.models import User


class UserTestCase(APITestCase):
    """Test users API."""

    def setUp(self):
        self.user = User.objects.create(email="test@example.com")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_user_create(self):
        """Testing user registration."""

        url = reverse("users:register")
        data = {
            "email": "user@example.com",
            "password": "1password1"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.all().count(), 2)
