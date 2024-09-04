from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from employees.models import Employee
from tasks.models import Task
from users.models import User


class TaskTestCase(APITestCase):
    """Test task API."""

    def setUp(self):
        self.user = User.objects.create(email="test@example.com")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.task = Task.objects.create(
            title="Test task",
            employee=None,
            deadline=None,
            status=Task.STATUS_ACTIVE,
            parent=None,
            user=self.user,
        )

    def test_task_create(self):
        """Testing adding a task."""

        url = reverse("tasks:task_create")
        data = {
            "title": "New task",
            "status": "0",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.all().count(), 2)
        self.assertEqual(response.json()['title'], 'New task')

    def test_task_update(self):
        """Testing a partial task update."""

        url = reverse("tasks:task_update", args=(self.task.pk,))
        data = {
            "title": "Updated title",
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), "Updated title")

    def test_task_delete(self):
        """Task removal testing."""

        url = reverse("tasks:task_delete", args=(self.task.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.all().count(), 0)

    def test_task_list(self):
        """Testing getting a list of tasks."""

        url = reverse("tasks:task_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_task_important_list(self):
        """Testing getting a list of important tasks."""

        employee = Employee.objects.create(
            full_name="employee",
            position="tester"
        )
        Task.objects.create(
            title="Subtask",
            employee=employee,
            deadline=None,
            status=Task.STATUS_ACTIVE,
            parent=self.task,
            user=self.user,
        )

        url = reverse("tasks:task_list_important")
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data[0]['available_employees'], ['employee'])
