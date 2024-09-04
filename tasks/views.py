from rest_framework.generics import ListAPIView, CreateAPIView, \
    UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from tasks.models import Task
from tasks.serializers import TaskCreateSerializer, TaskSerializer, \
    TaskImportantSerializer


# Create your views here.

class TaskListAPIView(ListAPIView):
    """View a list of tasks."""

    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated]


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
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()


class TaskRetrieveAPIView(RetrieveAPIView):
    """View task detail."""

    serializer_class = TaskCreateSerializer
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated]


class TaskDestroyAPIView(DestroyAPIView):
    """Destroy task."""

    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated]


class TaskImportantListAPIView(ListAPIView):
    """Returns a list of important tasks."""

    serializer_class = TaskImportantSerializer
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(
            children__employee__isnull=False,
            children__status=0,
            employee__isnull=True,
            status=0
        )
