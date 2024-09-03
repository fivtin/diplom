from rest_framework.generics import ListAPIView, CreateAPIView, \
    UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from tasks.models import Task
from tasks.serializers import TaskCreateSerializer, TaskSerializer, \
    TaskImportantSerializer
from users.permissions import IsOwner


# Create your views here.

class TaskListAPIView(ListAPIView):
    """View a list of tasks."""

    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated]
    # pagination_class = HabitPagination


class TaskCreateAPIView(CreateAPIView):
    """Create task."""

    serializer_class = TaskCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        task = serializer.save(user=self.request.user)
        task.save()


class TaskUpdateAPIView(UpdateAPIView):
    """Update task data."""

    serializer_class = TaskCreateSerializer
    permission_classes = [IsOwner]
    queryset = Task.objects.all()


class TaskRetrieveAPIView(RetrieveAPIView):
    """View task detail."""

    serializer_class = TaskCreateSerializer
    queryset = Task.objects.all()
    permission_classes = [IsOwner]


class TaskDestroyAPIView(DestroyAPIView):
    """Destroy task."""

    queryset = Task.objects.all()
    permission_classes = [IsOwner]


class TaskImportantListAPIView(ListAPIView):
    serializer_class = TaskImportantSerializer
    queryset = Task.objects.all()
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(
            children__employee__isnull=False,
            children__status=0,
            employee__isnull=True,
            status=0
        )
        # self.queryset = Task.objects.filter(
        #     Q(status=0),
        #     Q(parent__status=Task.STATUS_IN_PROGRESS),
        # )
        # return self.queryset

    # def get_queryset(self):
    #     return (Task.objects.annotate(
    #         active_tasks_count=Count('tasks', filter=Q(tasks__status=0))
    #     )
    #             # .filter(active_tasks_count__gt=0)
    # .order_by('-active_tasks_count'))
