from django.urls import path

from tasks.apps import TasksConfig
from tasks.views import TaskListAPIView, TaskCreateAPIView, TaskUpdateAPIView, TaskRetrieveAPIView, TaskDestroyAPIView, \
    TaskImportantListAPIView

app_name = TasksConfig.name

urlpatterns = [
    path('', TaskListAPIView.as_view(), name='task_list'),
    path('create/', TaskCreateAPIView.as_view(), name='task_create'),
    path('<int:pk>/update/', TaskUpdateAPIView.as_view(), name='task_update'),
    path('<int:pk>/', TaskRetrieveAPIView.as_view(), name='task_view'),
    path('<int:pk>/delete/', TaskDestroyAPIView.as_view(), name='task_delete'),
    path('important/', TaskImportantListAPIView.as_view(), name='task_list_important'),
]
