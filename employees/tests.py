from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from employees.models import Employee
from tasks.models import Task
from users.models import User


class EmployeeTestCase(APITestCase):
    """Test employee API."""

    def setUp(self):
        self.user = User.objects.create(email="admin@example.com")
        self.user.is_staff = True
        self.user.is_active = True
        self.user.is_superuser = True
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.employee = Employee.objects.create(
            full_name="employee",
            position="tester"
        )

    def test_employee_create(self):
        """Testing adding an employee."""

        url = reverse("employees:employee_create")
        data = {
            "full_name": "colleague",
            "position": "assistant",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employee.objects.all().count(), 2)
        self.assertEqual(response.json()['position'], 'assistant')

    # def test_employee_wrong_create(self):
    #     """Testing adding a employee."""
    #
    #     url = reverse("employee:employee_create")
    #     data = {
    #         "action": "action",
    #         "place": "place",
    #         "related_to": 1,
    #         "reward": "reward"
    #     }
    #     response = self.client.post(url, data)
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_employee_update(self):
        """Testing a partial employee update."""

        url = reverse("employees:employee_update", args=(self.employee.pk,))
        data = {
            "full_name": "also an employee",
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("full_name"), "also an employee")

    def test_employee_delete(self):
        """Employee removal testing."""

        url = reverse("employees:employee_delete", args=(self.employee.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Employee.objects.all().count(), 0)

    def test_employee_list(self):
        """Testing getting a list of employees."""

        url = reverse("employees:employee_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)

    def test_employee_list_with_active_tasks(self):
        """Testing getting a list of employees with active tasks."""

        task = Task.objects.create(
            title="Test task",
            employee=self.employee,
            deadline=None,
            status=Task.STATUS_ACTIVE,
            parent=None,
            user=self.user,
        )

        url = reverse("employees:employee_list_active_task")
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data[0]["active_tasks_count"], 1)
