from django.db.models import Count, Q
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

from employees.models import Employee
from employees.serializers import EmployeeSerializer, EmployeeTaskSerializer  # , EmployeeCreateSerializer
from users.permissions import IsOwner


# Create your views here.

class EmployeeListAPIView(ListAPIView):
    """View a list of employees."""

    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    permission_classes = [AllowAny]
    # pagination_class = HabitPagination

    # def get_queryset(self):
    #     queryset = Habit.objects.filter(user=self.request.user)
    #     return queryset


class EmployeeCreateAPIView(CreateAPIView):
    """Create employee."""

    # serializer_class = EmployeeCreateSerializer
    serializer_class = EmployeeSerializer
    permission_classes = [IsAdminUser]

    # def perform_create(self, serializer):
    #     employee = serializer.save(user=self.request.user)
    #     employee.save()


class EmployeeUpdateAPIView(UpdateAPIView):
    """Update employee data."""

    # serializer_class = EmployeeCreateSerializer
    serializer_class = EmployeeSerializer
    permission_classes = [IsAdminUser]
    queryset = Employee.objects.all()


class EmployeeRetrieveAPIView(RetrieveAPIView):
    """View employee detail."""

    # serializer_class = EmployeeCreateSerializer
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    permission_classes = [IsAdminUser]


class EmployeeDestroyAPIView(DestroyAPIView):
    """Destroy employee."""

    queryset = Employee.objects.all()
    permission_classes = [IsAdminUser]


class EmployeeTaskListAPIView(ListAPIView):
    """View a list of employees with tasks."""

    queryset = Employee.objects.all()
    serializer_class = EmployeeTaskSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return (Employee.objects.annotate(
            active_tasks_count=Count('tasks', filter=Q(tasks__status=0))
        )
                .filter(active_tasks_count__gt=0)
                .order_by('-active_tasks_count'))

    # pagination_class = HabitPagination

    # def get_queryset(self):
    #     queryset = Habit.objects.filter(user=self.request.user)
    #     return queryset
