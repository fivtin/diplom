from django.db.models import Count, Q
from rest_framework.generics import ListAPIView, CreateAPIView, \
    UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from employees.models import Employee
from employees.serializers import EmployeeSerializer, EmployeeActiveTaskSerializer


# Create your views here.

class EmployeeListAPIView(ListAPIView):
    """View a list of employees."""

    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    permission_classes = [IsAuthenticated]


class EmployeeCreateAPIView(CreateAPIView):
    """Create employee."""

    serializer_class = EmployeeSerializer
    permission_classes = [IsAdminUser]


class EmployeeUpdateAPIView(UpdateAPIView):
    """Update employee data."""

    serializer_class = EmployeeSerializer
    permission_classes = [IsAdminUser]
    queryset = Employee.objects.all()


class EmployeeRetrieveAPIView(RetrieveAPIView):
    """View employee detail."""

    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    permission_classes = [IsAdminUser]


class EmployeeDestroyAPIView(DestroyAPIView):
    """Destroy employee."""

    queryset = Employee.objects.all()
    permission_classes = [IsAdminUser]


class EmployeeActiveTaskListAPIView(ListAPIView):
    """View a list of employees with active tasks sorted by number of tasks."""

    queryset = Employee.objects.all()
    serializer_class = EmployeeActiveTaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return (Employee.objects.annotate(
            active_tasks_count=Count('tasks', filter=Q(tasks__status=0))
        )
                .filter(active_tasks_count__gt=0)
                .order_by('-active_tasks_count'))
